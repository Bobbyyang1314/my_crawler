import pymongo
import csv
import pandas as pd



my_client = pymongo.MongoClient("mongodb+srv://BobbyYang:001013@cluster0.gj8mcgv.mongodb.net/test")
mydb = my_client["mydatabase"]
mycol = mydb["customers"]

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 200)
df = pd.read_csv("courses.csv")

# exit()

df_t = df.head(100).T.to_dict().values()

for video in df_t:
    mycol.insert_one(video)
