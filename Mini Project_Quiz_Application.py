import random
print("Welcome to the 🎮 Video Games & Pop Culture Quiz")

# Store all questions inside a list of dictionaries
Question_Storage = [
    {"Question": "Which company created Mario?",
        "Options": "\nA. Sega \nB. Nintendo \nC. Sony \nD. Capcom", "Answer": "B"},
    {"Question": "In Minecraft, what material do you need to build a Nether Portal?",
        "Options": "\nA. Diamond \nB. Obsidian \nC. Bedrock \nD. Iron", "Answer": "B"},
    {"Question": "What is the name of the main protagonist in The Legend of Zelda series?",
        "Options": "\nA. Zelda \nB. Ganon \nC. Link \nD. Epona", "Answer": "C"},
    {"Question": "Which game popularized the Battle Royale genre worldwide?",
        "Options": "\nA. Fortnite \nB. Apex Legends \nC. PUBG \nD. Call of Duty Warzone", "Answer": "C"},
    {"Question": "In Grand Theft Auto V, how many playable protagonists are there?",
        "Options": "\nA. 1 \nB. 2 \nC. 3 \nD. 4", "Answer": "C"},
    {"Question": "Which console introduced motion controls with the Wii Remote?",
        "Options": "\nA. PlayStation 2 \nB. Xbox 360 \nC. Nintendo Wii \nD. PlayStation 3", "Answer": "C"},
    {"Question": "In Pokémon, what type is Pikachu?",
        "Options": "\nA. Fire \nB. Electric \nC. Normal \nD. Psychic", "Answer": "B"},
    {"Question": "Which game features the phrase “The cake is a lie”?",
        "Options": "\nA. Half-Life \nB. Portal \nC. BioShock \nD. Doom", "Answer": "B"},
    {"Question": "Who is the main character of the Halo series?",
        "Options": "\nA. Commander Shepard \nB. Doom Slayer \nC. Master Chief \nD. Marcus Fenix", "Answer": "C"},
    {"Question": "What does NPC stand for in gaming?",
        "Options": "\nA. Non-Playable Character \nB. Network Player Client \nC. New Player Controller \nD. Non-Player Computer", "Answer": "A"}
]

random.shuffle(Question_Storage) #Shuffles the order of the questions on each attempt

def check_answer(user,correct):
    return user == correct

def ask_question(Question_Storage):
    max_attempts = 3
    attempts_used = 0

    print("\n" + Question_Storage["Question"])
    print(Question_Storage["Options"])

    while attempts_used < max_attempts:
        user = input("Your answer: ").strip().upper()  # Prompts the user to enter an answer(strip removes space and upper converts the input to upper case)

        if user not in ["A","B","C","D"]:   #Accounts for invalid output
            print("Invalid input. Use A-D")
            continue

        attempts_used += 1

        if check_answer(user,Question_Storage["Answer"]): #checks if answers are correct
            print("Correct!")
            return True, attempts_used #correct, attempts used
        
        if attempts_used < max_attempts:
            print(f"Incorrect! {max_attempts - attempts_used} tries left")

    print(f"Out of tries! Correct answer was {Question_Storage['Answer']}")
    return False, attempts_used #incorrect, used all attempts
 
def show_results(total_score,total_questions,total_attempts): #Function to show the final results
    print("\n===== FINAL RESULTS =====")
    print("Questions:", total_questions)
    print("Correct:", total_score)
    print("Attempts Used:", total_attempts)
    print("Score %:", round((total_score/total_questions)*100, 2))
  
        
total_score = 0
total_attempts = 0

for question in Question_Storage: 
    correct, attempts_used = ask_question(question)
    total_attempts += attempts_used
    if correct:
        total_score += 1   #Adds 1 for each correct answer

show_results(total_score,len(Question_Storage),total_attempts) 

# Draft of MVP project (No Functions)
           
# for index, question in enumerate(Question_Storage, start=1): # loops the items/questions in the list and numbers them starting at 1
#     print(f"\nQuestion {index}: {question['Question']}") # Prints the question from the dictionary
#     print(question['Options']) # Prints the corresponding options
#     user_answer = input("\nYour answer: ").strip().upper() # Prompts the user to enter an answer(strip removes space and upper converts the input to upper case)
#     if user_answer == question['Answer']:
#         print("✓ Correct!") 
#     elif user_answer != question['Answer'] and user_answer in ["A", "B", "C", "D"]:
#          attempts = 2
#          for i in range(attempts,0,-1):
#             print(f"✗ Incorrect! {i} tries remaining")
#             user_answer = input("\nYour answer: ").strip().upper()

#             while i == 1:
#                 print(f"✗ Incorrect! No attempts remaining. The correct answer is {question['Answer']}")
#                 break

#             if user_answer == question['Answer']:
#                 print("✓ Correct!") 
#                 break
#     else:
#         if user_answer not in ["A", "B", "C", "D"]:
#             print("Invalid Answer. Please enter a valid response(A-D)")
#             attempts = 2
#             for i in range(attempts,0,-1):
#                 print(f" {i} tries remaining")
#                 user_answer = input("\nYour answer: ").strip().upper()

#                 while i == 1:
#                     print(f"No attempts remaining. The correct answer is {question['Answer']}")
#                     break

#                 if user_answer == question['Answer']:
#                     print("✓ Correct!") 
#                     break

    
    


    
    
