from pymongo import MongoClient
import os

client = MongoClient("mongodb+srv://user_tst_1:aaa@mongodblearning.bafyb7n.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
print(client.list_database_names())
db = client["rpg"]
collection = db["token_rpg"]
# collection.insert_one({"token":"user","privileges":"1"})
# for i in range(350):
#        collection.delete_one({"token":"user","privileges":"1"})
script_finalgress = {'ㄎㄎ長線':13, '兇靈線':15, '大學長線':15, '巫師線':15, '李日凱線':11}
script_wholeprogress = {'ㄎㄎ長線':[{"event":1,"choise":0}, {"event":2,"choise":0}, {"event":3,"choise":0}, {"event":4,"choise":0}, {"event":5,"choise":0},{"event":6,"choise":0},
                               {"event":7,"choise":0}, {"event":7,"choise":1}, {"event":8,"choise":0},{"event":9,"choise":0},{"event":10,"choise":0},{"event":11,"choise":0},
                               {"event":12,"choise":0},{"event":13,"choise":0}],
                        '兇靈線':[{"event":1,"choise":0}, {"event":2,"choise":0}, {"event":3,"choise":0}, {"event":4,"choise":0}, {"event":5,"choise":0},{"event":6,"choise":0},
                               {"event":7,"choise":0}, {"event":7,"choise":1}, {"event":8,"choise":0},{"event":9,"choise":0},{"event":10,"choise":0},{"event":11,"choise":0},
                               {"event":12,"choise":0},{"event":13,"choise":0},{"event":14,"choise":0},{"event":14,"choise":1},{"event":14,"choise":2},{"event":15,"choise":0}],
                        '大學長線':[{"event":1,"choise":0}, {"event":2,"choise":0}, {"event":3,"choise":0}, {"event":4,"choise":0}, {"event":5,"choise":0},{"event":6,"choise":0},
                               {"event":7,"choise":0}, {"event":8,"choise":0}, {"event":8,"choise":1},{"event":9,"choise":0},{"event":10,"choise":0},{"event":11,"choise":0},
                               {"event":12,"choise":0},{"event":13,"choise":0},{"event":14,"choise":0},{"event":15,"choise":0}],
                        '巫師線':[{"event":1,"choise":0}, {"event":2,"choise":0}, {"event":3,"choise":0}, {"event":4,"choise":0}, {"event":5,"choise":0},{"event":6,"choise":0},
                               {"event":6,"choise":1}, {"event":7,"choise":0}, {"event":8,"choise":0},{"event":9,"choise":0},{"event":10,"choise":0},{"event":11,"choise":0},
                               {"event":12,"choise":0},{"event":13,"choise":0},{"event":14,"choise":0},{"event":15,"choise":0}],
                        '李日凱線':[{"event":1,"choise":0}, {"event":2,"choise":0}, {"event":3,"choise":0}, {"event":3,"choise":1}, {"event":4,"choise":0}, {"event":5,"choise":0},{"event":6,"choise":0},
                               {"event":7,"choise":0}, {"event":8,"choise":0}, {"event":8,"choise":1}, {"event":8,"choise":2}, {"event":8,"choise":3}, {"event":9,"choise":0},{"event":10,"choise":0},{"event":11,"choise":0},]
                               }
index_path=os.path.dirname(os.path.abspath(__file__))