# try:
from kafka import KafkaProducer
from faker import Faker
import json
from time import sleep
# except Exception as e:
#     pass

producer = KafkaProducer(bootstrap_servers=['localhost:9200'], 
    # api_version=(0,11,5)
    )
_instance = Faker()


for _ in range(20):
    _data = {
        "first_name": _instance.first_name(),
        "city":_instance.city(),
        "phone_number":_instance.phone_number(),
        "state":_instance.state(),
        "id":str(_)
    }
    _payload = json.dumps(_data).encode("utf-8")
    response = producer.send('test_first2', _payload)
    print(response)
    # print(_payload)

    sleep(2)