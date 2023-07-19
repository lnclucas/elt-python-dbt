import requests, json, flatdict

class ApiConsumer():
    def get_data(self,url,request_type='GET'):
        response = requests.request(request_type,url)
        return json.loads(response.text)

    def normalize_data(self,data):
        return list(map(self.flatten_dict,data))

    def flatten_data_records(self,data_list):

        delimiter = ' | '
        data_list_obj_type = type(data_list[0])

        if data_list_obj_type == dict:
            new_dict = {}
            for record in data_list:
                for key in record.keys():
                    if key in new_dict.keys():
                        if type(record[key]) == list:
                            new_dict[key] += f"{delimiter.join([str(x) for x in record[key]])}"
                        elif type(record[key]) == dict:
                            new_dict[key].append(record[key])
                        else:
                            new_dict[key] += f" {delimiter} {record[key]}"
                    else:
                        if type(record[key]) == list:
                            new_dict[key] = f"{delimiter.join([str(x) for x in record[key]])}"
                        elif type(record[key]) == dict:
                            new_dict[key] = [record[key]]
                        else:
                            new_dict[key] = str(record[key])
            return new_dict
        else:
            return f"{delimiter.join([str(x) for x in data_list])}"
    
    def flatten_dict(self,data):
        d = dict(flatdict.FlatDict(data,delimiter='.'))
        new_dict = d.copy()
        flat_again = False
        for key in d.keys():
            if type(d[key]) == list:
                next_level_list = d[key]
                if len(next_level_list) == 0:
                    del new_dict[key]
                elif len(next_level_list) == 1:
                    if type(next_level_list[0]) == dict:
                        new_dict[key] = next_level_list[0]
                        flat_again = True
                    else:
                        new_dict[key] = str(next_level_list[0])
                else:
                    tmp_dict = self.flatten_data_records(next_level_list)
                    new_dict[key] = tmp_dict
                    flat_again = True
        return new_dict if not flat_again else self.flatten_dict(new_dict)

