import json
my_dict={
    "people":[
        {
            "name":"Bob",
            "age":23,
            "weight":80
        },
        {
            "name":"Ben",
            "age":25,
            "weight":88
        },
        {
            "name":"Binny",
            "age":29,
            "weight":79
        }
    ]
}
json_string = json.dumps(my_dict,indent=4)

with open('my_data.json','w') as f:
    f.write(json_string)
