from api_consumer import ApiConsumer
import pandas as pd
from sqlalchemy import create_engine
from getpass import getpass
import json

password = getpass('Database Password:')

engine = create_engine(f'postgresql://postgres:{password}@localhost:5455/db')

ac = ApiConsumer()

url_launches = 'https://api.spacexdata.com/v3/launches'
url_rockets = 'https://api.spacexdata.com/v3/rockets'


rockets = ac.get_data(url_rockets)
rockets = ac.normalize_data(rockets)
df_rockets = pd.DataFrame(rockets)
df_rockets.columns = [col.replace('.','_') for col in df_rockets.columns]
df_rockets[['payload_weights_kg','payload_weights_lb']]
df_rockets['payload_weights_kg_collected'] = df_rockets['payload_weights_kg'].astype(str).str.replace(' ','').str.split('|')
df_rockets['payload_weights_lb_collected'] = df_rockets['payload_weights_lb'].astype(str).str.replace(' ','').str.split('|')
df_rockets['payload_weights_collected'] = df_rockets[['payload_weights_kg_collected','payload_weights_lb_collected']].to_dict(orient='records')
df_rockets['payload_weights_collected'] = df_rockets['payload_weights_collected'].apply(lambda x: json.dumps(x))
df_rockets = df_rockets.drop(['payload_weights_kg_collected','payload_weights_lb_collected'],axis='columns')

df_rockets.to_sql('rockets',con=engine,schema='bronze', if_exists='replace',index=False)




launches = ac.get_data(url_launches)
launches = ac.normalize_data(launches)
df_launches = pd.DataFrame(launches)
df_launches.columns = [col.replace('.','_') for col in df_launches.columns]
df_launches['payload_weights_collected'] = df_launches['rocket_second_stage_payloads_payload_id'].str.replace(' ','').str.split('|')

df_launches.to_sql('launches',con=engine,schema='bronze', if_exists='replace',index=False)