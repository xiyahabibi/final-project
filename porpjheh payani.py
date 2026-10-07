


 
password = "8907"



print("!!!!bazi hadseh ramz!!!!")
print("faghat 3 ta forsat darid")


success = False

for attempt in range(1, 4):
    guess = input("ramz ra vared koonid: ")

    if guess == password:
        print("ramz dorost bood")
        success = True
        break
    else:
        print("ramz eshtebahbood")
        print("tedad talash baghi mandeh:", 3 - attempt)

if success:
    print("khoosh omadid!")

    choice = input(
        "1. Shrooe bazi hadseh ramz \n"
        "2. Exit\n"
        "Entekhabeton: "
    )

    match choice:
        case "1":
            secret = "8907"
            max_guesses = 10

            print("bazi shooroe shood")
            print("10 forsat baghi mandeh")

            for attempt in range(1, max_guesses + 1):
                guess = input("hadseh shooma : ")

                if guess == secret:
                    print("sad afarin!.")
                    print("talash hae estefadeh shoodeh:", attempt)
                    break
                else:
                    print("ramz eshtebah bood")
                    print("tedad hadseh baghi mandeh:",
                          max_guesses - attempt)
            else:
                print("hads ha tamoom shood")
                print("ramz in bood:", secret)

        case "2":
            print("az barnameh kharej mishaveed")

        case _:
            print("entekhab dorost nist")

else:
    print("seh bar talash kardi va vared nashoodi")

    secret = "5678"
    max_guesses = 10

    print("bazi hads shooroe shood")
    print("10 forsat dari")

    for attempt in range(1, max_guesses + 1):
        guess = input("hadseh shooma: ")

        if guess == secret:
            print("sad afarin!")
            print("tedad hadseh estefadeh shoodeh:", attempt)
            break
        else:
            print("ramz ghalat bood")
            print("tedad hadseh baghi mandeh:",
                  max_guesses - attempt)
    else:
        print("hads hatoon tamoom shodan")
        print("ramz in bood:", secret)