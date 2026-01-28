def main():
	name = input("Please enter your name: ")
	raw_age = input("Please enter your age: ")

	if raw_age.isdigit():
		age = int(raw_age)
		print("Hello,", name)
		print("Next year you will be:", age + 1)
	else:
		print("Invalid age input. Please enter a number.")
		



if __name__ == "__main__":
	main()