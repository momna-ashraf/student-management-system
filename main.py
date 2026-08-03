def display_menu():
    print("\n========== Student Management System ============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    while True:
          display_menu()
          try:
             choice = int(input("\nEnter your choice: "))
          except ValueError:
              print("Please enter a valid number.")
              continue

          if choice == 1:
             print("Feature coming soon...")

          elif choice == 2:
             print("Feature coming soon...")

          elif choice == 3:
             print("Feature coming soon...")

          elif choice == 4:
             print("Feature coming soon...")

          elif choice == 5:
             print("Feature coming soon...")

          elif choice == 6:
             print("Thank you for using Student Management System")
             break
          else:
             print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()