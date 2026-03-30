contact = {}

print("Welcome to the contact book!")
print("You can add, view, and delete contacts.")

while True:
  print("\nOptions:")
  print("1. Add a contact")
  print("2. View all contacts")
  print("3. Delete a contact")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == "1":
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    contact[name] = phone
    print("Contact added successfully!")
  elif choice == "2":
    print("All contacts:")
    for name, phone in contact.items():
      print(f"{name}: {phone}")
  elif choice == "3":
    name = input("Enter the name of the contact to delete: ")
    if name in contact:
      del contact[name]
      print("Contact deleted successfully!")
    else:
      print("Contact not found.")
  elif choice == "4":
    print("Exiting the contact book. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")

