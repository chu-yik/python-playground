user_id_to_name = {
	715: "Annie",
	901: "Natalie",
	1213: "Athena"
}

# get() method on dicts and "default" arguement
def greeting(user_id):
	return "Hi {0}".format(user_id_to_name.get(user_id, 'there'))

print(greeting(901))
print(greeting(123))
