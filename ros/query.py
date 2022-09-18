import pickle
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ros2-topics-messages')
response = table.get_item(
    Key={
        '_id': "6189b09f-b170-4692-81dc-24b85689bb7b",
    }
)
item = response['Item']["payload"]

# method 1
data = pickle.loads(bytes(item))

# method 2
# with open("test.pkl", "wb") as f:
#     f.write(bytes(item))

# data = pickle.load(open("test.pkl", "rb"))

print(str(data))
# print(table.creation_date_time)
# dict_a = {'A': 0, 'B': 1, 'C': 2}
# pickle.dump(dict_a, open('test.pkl', 'wb'))
# my_dict = pickle.load(open('./test.pkl', 'rb'))
# print(my_dict)pip
