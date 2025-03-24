def NULL_not_found(object: any) -> int:
	obj_type = type(object)
	if(obj_type is type(None)):
		print(f"Nothing: None {obj_type}")
	elif(obj_type is float):
		print(f"Cheese: nan {obj_type}")
	elif(obj_type is int):
		print(f"Zero: 0 {obj_type}")
	elif(obj_type is str and len(object) == 0):
		print(f"Empty: {obj_type}")
	elif(obj_type is bool and object == False):
		print(f"Fake: False {obj_type}")
	else:
		print("Type not Found")
		return (1)
	return (0)		