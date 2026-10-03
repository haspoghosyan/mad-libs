import random

choice = input("Please choose a template: 1, 2, or 3: ")

if choice == "1" or choice == "2" or choice == "3":

    story_type = random.choice(["hospital", "camping", "castle"])

    if story_type == "hospital":

        number = input("Enter a number: ")
        measure_of_time = input("Enter a measure of time: ")
        transportation = input("Enter a mode of transportation: ")
        adjective = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        noun = input("Enter a noun: ")
        color = input("Enter a color: ")
        body_part = input("Enter a part of the body: ")
        verb = input("Enter a verb: ")
        number2 = input("Enter another number: ")
        noun2 = input("Enter another noun: ")
        noun3 = input("Enter another noun: ")
        body_part2 = input("Enter another part of the body: ")
        verb2 = input("Enter another verb: ")
        noun4 = input("Enter another noun: ")
        adjective3 = input("Enter another adjective: ")
        silly_word = input("Enter a silly word: ")
        noun5 = input("Enter a noun: ")

        story = (
            f"It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transportation}."
            f"The hospital is a/an {adjective} place,there are a lot of {adjective2} {noun} here."
            f"There are nurses here who have {color} {body_part}. If someone wants to come into my room I told them that they have to {verb} first."
            f"I've decorated my room with {number2} {noun2}. "
            f"Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
            f"I heard that all doctors {verb2} {noun4} every day for breakfast. "
            f"The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!"
        )

    elif story_type == "camping":

        person_name = input("Enter a person's name: ")
        noun = input("Enter a noun: ")
        adjective = input("Enter an adjective describing a feeling: ")
        verb = input("Enter a verb: ")
        adjective2 = input("Enter another adjective describing a feeling: ")
        animal = input("Enter an animal: ")
        verb2 = input("Enter another verb: ")
        color = input("Enter a color: ")
        verb_ing = input("Enter a verb ending in -ing: ")
        adverb = input("Enter an adverb ending in -ly: ")
        number = input("Enter a number: ")
        measure_of_time = input("Enter a measure of time: ")
        color2 = input("Enter a color: ")
        animal2 = input("Enter another animal: ")
        number2 = input("Enter a number: ")
        silly_word = input("Enter a silly word: ")
        noun2 = input("Enter another noun: ")

        story = (
            f"This weekend I am going camping with {person_name}. I packed my lantern,sleeping bag, and {noun}. "
            f"I am so {adjective} to {verb} in a tent. "
            f"I am {adjective2} we might see a(n) {animal}, I hear they're kind of dangerous. "
            f"While we're camping, we are going to hike, fish, and {verb2}. "
            f"I have heard that the {color} lake is great for {verb_ing}. "
            f"Then we will {adverb} hike through the forest for {number} {measure_of_time}. "
            f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! "
            f"At night we will tell {number2} {silly_word} stories and roast {noun2} round the campfire!!"

        )

    elif story_type == "castle":

        person_name = input("Enter a person's name: ")
        adjective = input("Enter an adjective: ")
        color = input("Enter a color: ")
        animal = input("Enter an animal: ")
        place = input("Enter a place: ")
        adjective2 = input("Enter another adjective: ")
        magical_creature = input("Enter a plural magical creature: ")
        adjective3 = input("Enter another adjective: ")
        magical_creature2 = input("Enter another plural magical creature: ")
        room = input("Enter a room in a house: ")
        noun = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        noun_plural3 = input("Enter a plural noun: ")
        adjective4 = input("Enter another adjective: ")
        noun_plural4 = input("Enter another plural noun: ")
        number = input("Enter a number: ")
        measure_of_time = input("Enter a measure of time: ")
        verb_ing = input("Enter a verb ending in -ing: ")
        adjective5 = input("Enter another adjective: ")
        noun5 = input("Enter another noun: ")

        story = (
            f"Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest."
            f"I found myself here one day after going for a ride on a {color} {animal} in {place}."
            f"There are {adjective2} {magical_creature} and {adjective3} {magical_creature2} here!"
            f"In the {room} there is a pool full of {noun}."
            f"I fall asleep each night on a {noun2} of {noun_plural3} and dream {adjective4} {noun_plural4}. "
            f"It feels as though I have lived here for {number} {measure_of_time}. "
            f"I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!"

        )

    print()
    print("Your story:")
    print(story)

else:
    print("Invalid template number.")