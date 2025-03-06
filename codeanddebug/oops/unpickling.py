import pickle

with open("person.pickle", "rb") as f:
    data = pickle.load(f)
print(data)
