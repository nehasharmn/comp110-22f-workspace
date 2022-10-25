"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary 
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# Set a key-value parining in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation 
print(schools)

# Access a vallue by its key -- "lookup"
print (f"UNC has {schools['UNC']} students")

# Remove a key value pair from a dictionary 
# by its key
schools.pop("Duke")                    

# Test for the existence of a key 
is_duke_present: bool = "Duke" in schools 
print(f" Duke is present: {is_duke_present}")
print(schools)

# Update/ reassignt a key-value pair 
schools["UNC"] = 20000
schools["NCSU"] =+ 200
print(schools)

# Empty dictionary
schools = {} # same as dict ()

#Alternatively intialize key-value pairs 
schools = {"UNC": 194000, "DUokie": 6717, "NCSU": 26150}
print(schools)

# WHAT HAPPENS WHEN A KEY DOES NOT EXIST
#print(schools["UNCC"])
# example looping over keys of a dict 
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")


letter: dict[str,int] = {1:"a",2:"c",3:"d"}
for value in letter:
    print(value)