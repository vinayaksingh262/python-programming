import pickle

person = {"name": "alice", "age": 20}
with open("person.pickle", "wb") as f:
    pickle.dump(person, f)
print("pickling completed")
