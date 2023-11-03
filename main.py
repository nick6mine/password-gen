import string
import random

art = r'''
__________                                               .___   ________                                   __                
\______   \_____    ______ ________  _  _____________  __| _/  /  _____/  ____   ____   ________________ _/  |_  ___________ 
 |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |  /   \  ____/  __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
 |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |  \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |   \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
                \/     \/     \/                          \/          \/     \/     \/     \/           \/                   
'''
print(art)


def generate_random_string(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  random_string = ''.join(random.choice(characters) for _ in range(length))
  return random_string


def save_password_to_file(password):
  with open("passwords.txt", "a") as file:
    file.write("Password: " + password + "\n")


while True:
  decision = input(
      "\nEnter 'r' to generate a random password or 's' to enter your own (or 'q' to quit): "
  )

  if decision == "r":
    yes = int(input("\nChoose a length for the random password: "))
    randString = generate_random_string(yes)
    print("\nRandom Password: ", randString, "\n")
    save_password_to_file(randString)
  elif decision == "s":
    firstName = input("\nEnter your first name: ")
    lastName = input("\nEnter your last name: ")
    birthYear = input("\nEnter your birth year: ")
    customCharacters = input("\nEnter your custom characters: ")
    variables = [firstName, lastName, birthYear, customCharacters]
    random.shuffle(variables)
    password = ''.join(variables)
    print("\nYour password is: ", password)
    save_password_to_file(password)
  elif decision == "q":
    print("\nQuitting the password generator. Goodbye!")
    break
  else:
    print("Invalid choice. Please enter 'r', 's', or 'q' to quit.")
