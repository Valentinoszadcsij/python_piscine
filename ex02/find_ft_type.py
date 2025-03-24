def all_thing_is_obj(object: any) -> int:
		obj_type = type(object)
		if  obj_type is int:
			print("Type not found")
		else:
			if obj_type is str:
				print(f"{object} is in the kitchen : {str(obj_type)}")
			else:
				print(f"{str(obj_type.__name__).capitalize()} : {str(obj_type)}")
		return (42)