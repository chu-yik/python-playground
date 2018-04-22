import operator 

dict = {
	'a': 4,
	'b': 2,
	'c': 3,
	'd': 1
}

print("original dict: {0}".format(dict))
print("original dict, items: {0}".format(dict.items()))

# key=lambda is like creating sorting func without name def, params: return
# https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
sort_dict = sorted(dict.items(), key=lambda x: x[1])
print("sorted by value {0}".format(sort_dict))

# or alternatively
def sort_by_val(kvp):
	return kvp[1]

new_dict = sorted(dict.items(), key=sort_by_val)
print("my ver - sorted by value {0}".format(new_dict))

# or using operator
op_dict = sorted(dict.items(), key=operator.itemgetter(1))
print("operator sort {0}".format(op_dict))
