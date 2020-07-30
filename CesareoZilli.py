import pymongo
import urllib.request, json

url_api = 'https://api.bsmsa.eu/ext/api/bsm/gbfs/v2/en/station_status'
with urllib.request.urlopen(url_api) as url:
    archivo = json.loads(url.read().decode())

client = pymongo.MongoClient("mongodb+srv://cesar:cesar@cluster0.9eiwd.mongodb.net/bbdd_prueba?retryWrites=true&w=majority")
db = client.bbdd_prueba
coleccion = db.coleccion

coleccion.insert_one(data)

def bikes():
    print("\n\n Bicicletas disponbles")
    available = coleccion.find({'num_bikes_available': "14"})
    for i in available:
         print(i)
bikes()

def top():
    print('\n\n Top 3 ')
    datostop = coleccion.find().sort([("station_id", 1)]).limit(3)
    for top3 in datostop:
        print(top3)
top()

media = coleccion.aggregate([
        {"$group":
             {"_id":"null",
             "Disponibles":{ "$avg": "num_docks_available" }
              }
         }
    ])
print("\n\n media")
print(media)

