import random

MASTER_LIST = [['New York City', ' New York', ' 40.7128', ' 74.006'],
               ['Los Angeles', ' California', ' 34.0549', ' 118.2426'],
               ['Chicago', ' Illinois', ' 41.8781', ' 87.6298'],
               ['Houston', ' Texas', ' 29.7601', ' 95.3701'],
               ['Phoenix', ' Arizona', ' 33.4482', ' 112.0777'],
               ['Philadelphia', ' Pennsylvania', ' 39.9526', ' 75.1652'],
               ['San Antonio', ' Texas', ' 29.4252', ' 98.4946'],
               ['San Diego', ' California', ' 32.7157', ' 117.1611'],
               ['Dallas', ' Texas', ' 32.7767', ' 96.797'],
               ['Austin', ' Texas', ' 30.2672', ' 97.7431'],
               ['Jacksonville', ' Florida', ' 30.3298', ' 81.6592'],
               ['San Jose', ' California', ' 37.3387', ' 121.8853'],
               ['Fort Worth', ' Texas', ' 32.7555', ' 97.3308'],
               ['Columbus', ' Ohio', ' 39.9625', ' 83.0032'],
               ['Charlotte', ' North Carolina', ' 35.2216', ' 80.8401'],
               ['Indianapolis', ' Indiana', ' 39.7691', ' 86.158'],
               ['San Francisco', ' California', ' 37.7749', ' 122.4194'],
               ['Seattle', ' Washington', ' 47.6061', ' 122.3328'],
               ['Denver', ' Colorado', ' 39.7392', ' 104.9903'],
               ['Oklahoma City', ' Oklahoma', ' 35.4689', ' 97.5195'],
               ['Nashville', ' Tennessee', ' 36.1627', ' 86.7816'],
               ['El Paso', ' Texas', ' 31.7619', ' 106.485'],
               ['Washington', ' D.C.', ' 38.9072', ' 77.0369'],
               ['Las Vegas', ' Nevada', ' 36.1716', ' 115.1391'],
               ['Boston', ' Massachusetts', ' 42.3555', ' 71.0565']]

CITY_LIST = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin',
             'Jacksonville', 'San Jose', 'Fort Worth', 'Columbus', 'Charlotte',
             'Indianapolis', 'San Francisco', 'Seattle', 'Denver', 'Oklahoma City',
             'Nashville', 'El Paso', 'Washington', 'Las Vegas', 'Boston']

index = random.randrange(0,24)
mystery_city = CITY_LIST[index]
mystery_city_lat = MASTER_LIST[index][2]
mystery_city_long = MASTER_LIST[index][3]

print()
print("Welcome to Townle!")
print("To play, enter the name of a U.S. city to try and guess the mystery city.\nExit the game at anytime by guessing 'Exit'.\nThe game is case sensitive, so be sure to use capitalization!")
print()
print("For reference, the U.S. vertically spans roughly 35 degrees of latitude\nfrom 25° N to 49° N and horizontally spans roughly 135° of longitude\nfrom 67° W to 179° W.")
print()

hint = input("Would you like to see a list of valid cities? Yes or No: ")
if hint == "Yes":
    print()
    print(", ".join(CITY_LIST))
    print()
guess = input("Guess a city: ")
guess_count = 1
print()

while guess != mystery_city:
    if guess == "Exit":
        print(f"Thank you for playing. The mystery city was {mystery_city}. See you next time!")
        break
    if guess not in CITY_LIST:
        print("Sorry, that city is not programmed in yet.")
    else:
        for i in range(len(CITY_LIST)):
            if CITY_LIST[i] == guess:
                guess_lat = MASTER_LIST[i][2]
                guess_long = MASTER_LIST[i][3]
                break
        print()
        print(f"Not quite! The latitude coordinates of {guess} are{guess_lat}\nand the longitude coordinates are{guess_long}.")
        print()
        lat_diff = round(float(mystery_city_lat) - float(guess_lat), 4)
        long_diff = round(float(mystery_city_long) - float(guess_long), 4)
        if lat_diff < 0:
            lat_direc = "north"
        else:
            lat_direc = "south"
        if long_diff < 0:
            long_direc = "west"
        else:
            long_direc = "east"
        lat_diff = abs(lat_diff)
        long_diff = abs(long_diff)
        print(f"{guess} is {lat_diff} degrees {lat_direc} from the mystery city\nand {long_diff} degrees {long_direc} from the mystery city.")
        print()
    if guess_count > 5:
        give_up = input("Want to give up? Yes or No: ")
        if give_up == "Yes":
            print(f"Thank you for playing. The mystery city was {mystery_city}.")
            break
    guess = input("Guess another city: ")
    guess_count += 1
    
if guess == mystery_city:
    print()
    print("Congratulations, you guessed the mystery city!\nThank you for playing.")

