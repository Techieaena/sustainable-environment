import os

# -------- Contact Form Data Encryptor -------- #

# Encrypt function using Caesar Cipher
def encrypt_message(message):
    encrypted = ""
    for char in message:
        encrypted += chr(ord(char) + 3)
    return encrypted

# Main form function
def contact_form():
    submissions = []  # list to hold all contacts

    while True:
        print("\n--- Contact Form ---")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        message = input("Your message: ")

        if not name or not email or not message:
            print("All fields are required!")
            continue

        encrypted_message = encrypt_message(message)
        
        submission = {
            "name": name,
            "email": email,
            "message": encrypted_message
        }

        submissions.append(submission)

        another = input("Submit another entry? (yes/no): ").lower()
        if another != "yes":
            break

    return submissions

# Save to file
def save_to_file(data_list):
    try:
        # Ensure the 'data' folder exists
        os.makedirs("data", exist_ok=True)

        with open("data/contacts.txt", "w") as file:
            for contact in data_list:
                file.write(f"Name: {contact['name']}\n")
                file.write(f"Email: {contact['email']}\n")
                file.write(f"Encrypted Message: {contact['message']}\n")
                file.write("-" * 30 + "\n")
        print("Data saved to contacts.txt ✅")
    except Exception as e:
        print("Error saving file:", e)

# -------- Execution Starts Here -------- #
if __name__ == "__main__":
    all_data = contact_form()
    save_to_file(all_data)

