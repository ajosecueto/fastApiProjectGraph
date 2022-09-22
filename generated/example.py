from generated.proto import preferences_pb2

pref = preferences_pb2.Preference(name="demodemo")

with open("./serializedFile", "wb") as fd:
    fd.write(pref.SerializeToString())

pref = preferences_pb2.Preference()
with open("./serializedFile", "rb") as fd:
    pref.ParseFromString(fd.read())

print(pref)
