import random
import re
templates = [
    "Today I went to the zoo. I saw a(n) {adjective1} {animal1} jumping up and down in its cage. "
    "It {verb1} {adverb1} through the bars and ran into the {place1}. "
    "I was so {emotion1}, I dropped my {noun1}!",

    "It was a {adjective1} day, and I had just put on my {clothing1}. "
    "Suddenly, a {noun1} fell from the sky and {verb1} right in front of me! "
    "I ran all the way to the {place1}, hoping to find my {noun2}.",

    "At school today, my {adjective1} teacher told us to {verb1} in the hallway. "
    "Later, during lunch, I found a {adjective2} {food1} inside my backpack. "
    "My best friend and I {verb2} all the way to the {place1} to hide it.",

    "Captain {name1} was ready to launch into space aboard the {adjective1} rocket ship. "
    "But just before liftoff, a {animal1} ran across the control panel and {verb1} everything up! "
    "“{exclamation1}!” shouted the crew, as they floated toward {planet1}.",

    "Last night’s party at the {place1} was {adjective1}! "
    "Everyone wore {color1} hats and danced to {noun1} music. "
    "Suddenly, someone brought a {adjective2} {animal1} and it started to {verb1}!"
]
def main():
    while True:
        template_choice = random.choice(templates)
        blanks = re.findall(r"{(.*?)}", template_choice)
        user_inputs = {}

        for word in blanks:
            if word not in user_inputs: 
                while True:
                    user_input = input(f"Enter a {word.replace('_', ' ')}:").strip()
                    if user_input:
                        user_inputs[word] = user_input
                        break
                    else:
                        print("Please enter something!")

        final_story = template_choice.format(**user_inputs)

        print("\n🎉 Here's what the computer created from your words 🎉\n")
        print(final_story)
        print()

       
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()