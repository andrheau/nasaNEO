# This program stores information about pets. For each pet,
#   we store the kind of animal, the owner's name, and
#   the breed.
pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},
        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},
        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},
        }

# Let's show all the information for each pet.
for pet_name, pet_information in pets.items():
    print("\nHere is what I know about %s:" % pet_name.title())
    # Each animal's dictionary is in pet_information
    for key in pet_information:
        if key == 'owner':
            # Capitalize the owner's name.
            print(key + ": " + pet_information[key].title())
        elif key == 'vaccinated':
            # Print 'yes' for True, and 'no' for False.
            vaccinated = pet_information['vaccinated']
            if vaccinated:
                print ('vaccinated: yes')
            else:
                print ('vaccinated: no')
        else:
            # No special formatting needed for this key.
            print(key + ": " + pet_information[key])