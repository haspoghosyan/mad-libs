import random


def hospital_story():
    print("\nHospital Story")

    number = input("Type a number: ")
    time = input("Type a measure of time: ")
    transportation = input("Type a mode of transportation: ")
    adjective = input("Type an adjective: ")
    adjective2 = input("Type another adjective: ")
    noun = input("Type a noun: ")
    color = input("Type a color: ")
    body_part = input("Type a part of the body: ")
    verb = input("Type a verb: ")
    number2 = input("Type another number: ")
    noun2 = input("Type another noun: ")
    noun3 = input("Type another noun: ")
    body_part2 = input("Type another part of the body: ")
    verb2 = input("Type another verb: ")
    noun4 = input("Type another noun: ")
    adjective3 = input("Type another adjective: ")
    silly_word = input("Type a silly word: ")
    noun5 = input("Type another noun: ")

    print("\nYour story:")
    print(
        "It was about " + number + " " + time +
        " ago when I arrived at the hospital in a " + transportation +
        ". The hospital is a/an " + adjective +
        " place, there are a lot of " + adjective2 + " " + noun +
        " here. There are nurses here who have " + color + " " + body_part +
        ". If someone wants to come into my room I told them that they have to " +
        verb + " first. I've decorated my room with " + number2 + " " + noun2 +
        ". Today I talked to a doctor and they were wearing a " + noun3 +
        " on their " + body_part2 +
        ". I heard that all doctors " + verb2 + " " + noun4 +
        " every day for breakfast. The most " + adjective3 +
        " thing about being in the hospital is the " + silly_word + " " + noun5 + "!"
    )


def camping_story():
    print("\nCamping Story")

    name = input("Type a person's name: ")
    noun = input("Type a noun: ")
    feeling = input("Type an adjective describing a feeling: ")
    verb = input("Type a verb: ")
    feeling2 = input("Type another adjective describing a feeling: ")
    animal = input("Type an animal: ")
    verb2 = input("Type another verb: ")
    color = input("Type a color: ")
    verb_ing = input("Type a verb ending in -ing: ")
    adverb = input("Type an adverb ending in -ly: ")
    number = input("Type a number: ")
    time = input("Type a measure of time: ")
    color2 = input("Type another color: ")
    animal2 = input("Type another animal: ")
    number2 = input("Type another number: ")
    silly_word = input("Type a silly word: ")
    noun2 = input("Type another noun: ")

    print("\nYour story:")
    print(
        "This weekend I am going camping with " + name +
        ". I packed my lantern, sleeping bag, and " + noun +
        ". I am so " + feeling + " to " + verb +
        " in a tent. I am " + feeling2 +
        " we might see a(n) " + animal +
        ", I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and " +
        verb2 + ". I have heard that the " + color +
        " lake is great for " + verb_ing +
        ". Then we will " + adverb +
        " hike through the forest for " + number + " " + time +
        ". If I see a " + color2 + " " + animal2 +
        " while hiking, I am going to bring it home as a pet! At night we will tell " +
        number2 + " " + silly_word +
        " stories and roast " + noun2 + " around the campfire!!"
    )


def castle_story():
    print("\nCastle Story")

    name = input("Type a person's name: ")
    adjective = input("Type an adjective: ")
    color = input("Type a color: ")
    animal = input("Type an animal: ")
    place = input("Type a place: ")
    adjective2 = input("Type another adjective: ")
    creature = input("Type a magical creature (plural): ")
    adjective3 = input("Type another adjective: ")
    creature2 = input("Type another magical creature (plural): ")
    room = input("Type a room in a house: ")
    noun = input("Type a noun: ")
    noun2 = input("Type another noun: ")
    plural_noun3 = input("Type a plural noun: ")
    adjective4 = input("Type another adjective: ")
    plural_noun4 = input("Type another plural noun: ")
    number = input("Type a number: ")
    time = input("Type a measure of time: ")
    verb_ing = input("Type a verb ending in -ing: ")
    adjective5 = input("Type another adjective: ")
    noun5 = input("Type another noun: ")

    print("\nYour story:")
    print(
        "Dear " + name +
        ", I am writing to you from a " + adjective +
        " castle in an enchanted forest. I found myself here one day after going for a ride on a " +
        color + " " + animal + " in " + place +
        ". There are " + adjective2 + " " + creature +
        " and " + adjective3 + " " + creature2 +
        " here! In the " + room +
        " there is a pool full of " + noun +
        ". I fall asleep each night on a " + noun2 +
        " of " + plural_noun3 + " and dream of " +
        adjective4 + " " + plural_noun4 +
        ". It feels as though I have lived here for " + number +
        " " + time +
        ". I hope one day you can visit, although the only way to get here now is " +
        verb_ing + " on a " + adjective5 + " " + noun5 + "!"
    )


print("\nChoose one of the following stories:")
print("1: Hospital")
print("2: Camping")
print("3: Castle")
print("4: Random story")

choice = input("Enter your choice (1-4): ")


while choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Please try again.")
    choice = input("Enter your choice (1-4): ")

if choice == "1":
    hospital_story()

elif choice == "2":
    camping_story()

elif choice == "3":
    castle_story()

else:
    random_story = random.choice([hospital_story, camping_story, castle_story])
    random_story()
