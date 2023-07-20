select
	distinct 
    l.launch_site_site_id as "ID Plataforma",
	l.launch_site_site_name as "Cod. Plataforma Lanc." ,
	l.launch_site_site_name_long as "Desc. Plataforma Lanc."
from
	{{ source('raw', 'launches') }}  l