def main():

	users = [
		{"name": "Alice", "age": 15, "active": True} ,
		{"name": "Bob", "age": 22, "active": True},
		{"name": "Charlie", "age": 30, "active": True},
		{"name": "Daisy", "age": 17, "active": True},
		{"name": "Eve", "age": 40, "active": False},
	]

	print("Active adult users:")
	found_underage_active = False	

	for index, user in enumerate(users, start=1):

		if not user["active"]:
			continue

		if user["age"] < 18:
			found_underage_active = True
			continue
		
		print(index, user["name"], user["age"])		

	if found_underage_active:
		print("Warning: There is at least one underage active user!")
			


if __name__ == "__main__":
	main()