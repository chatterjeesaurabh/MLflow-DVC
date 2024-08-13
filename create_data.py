import pandas as pd

data = [
    {"name": "Saurabh", "age": 26, "city": "Varanasi"},
    {"name": "Krish", "age": 27, "city": "Delhi"},
    {"name": "Shubham", "age": 25, "city": "Mumbai"},
    {"name": "Aditya", "age": 29, "city": "Bangalore"},
    {"name": "Monu", "age": 23, "city": "Kolkata"},          # new data added 1
    {"name": "Naruto", "age": 21, "city": "Konoha"}          # new data added 2
]


df = pd.DataFrame(data)

df.to_csv("data/data.csv", index=False)


