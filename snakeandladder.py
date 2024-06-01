import random
import sys
from itertools import count

sys.setrecursionlimit(100000000)

rev_lst = [91, 90, 71, 70, 51, 50, 31, 30, 11, 10, 9]
main_lst = {}
flag = True
snake_dict = {}
sidi_dict = {}
for i in range(100, 0, -10):
    if flag:
        flag = False
        for i in range(i, i - 10, -1):
            # main_lst[i]=""
            main_lst[i] = {"trap": "", "tokens": ""}
    else:
        flag = True
        for i in range(i - 9, i + 1, 1):
            main_lst[i] = {"trap": "", "tokens": ""}


def print_snake_ladder():
    # counter = 0
    # lst = main_lst.keys()
    # values = list(main_lst.values())
    # flag = 0
    # for i in lst:
    #     if values[flag] == "":
    #         print(f"| {i} |", end="")
    #         flag += 1
    #     else:
    #         print(f"| {i} | |{values[flag]}|", end="")
    #         flag += 1
    #     counter += 1
    #     if counter == 10:
    #         print("\n")
    #         counter = 0
    counter = 0
    lst = main_lst.keys()
    for i in lst:
        if main_lst[i]["trap"] == "" and main_lst[i]["tokens"] == "":
            print(f"| {i} |", end="")
        elif main_lst[i]["trap"] != "" and main_lst[i]["tokens"] != "":
            print(f"| {i} | |{main_lst[i]['trap']}| |{main_lst[i]['tokens']}|", end="")
        elif main_lst[i]["tokens"] != "":
            print(f"| {i} | |{main_lst[i]['tokens']}|", end="")
        else:
            print(f"| {i} | |{main_lst[i]['trap']}|", end="")
        counter += 1
        if counter == 10:
            print("\n")
            counter = 0


snake_lst = []
sidi_lst = []


def rondom_number():
    return random.randint(2, 99)


def genrate_rondom_snake():
    n1 = rondom_number()
    n2 = rondom_number()

    if n1 in snake_lst or n2 in snake_lst:
        return genrate_rondom_snake()
    elif n1 + 1 in snake_lst or n1 - 1 in snake_lst:
        return genrate_rondom_snake()
    elif n2 + 1 in snake_lst or n2 - 1 in snake_lst:
        return genrate_rondom_snake()
    elif n1 == n2:
        return genrate_rondom_snake()
    elif n1 > n2:
        snake_lst.append(n1)
        snake_lst.append(n2)
        return [n1, n2]
    else:
        snake_lst.append(n2)
        snake_lst.append(n1)
        return [n2, n1]


def genrate_rondom_sidi():
    n1 = rondom_number()
    n2 = rondom_number()

    if (n1 in sidi_lst or n2 in sidi_lst) and (
        n1 not in snake_lst or n2 not in snake_lst
    ):
        genrate_rondom_sidi()
    elif (n1 + 1 in sidi_lst or n2 + 1 in sidi_lst) and (
        n1 not in snake_lst or n2 not in snake_lst
    ):
        genrate_rondom_sidi()
    elif (n1 - 1 in sidi_lst or n2 - 1 in sidi_lst) and (
        n1 not in snake_lst or n2 not in snake_lst
    ):
        genrate_rondom_sidi()
    if n1 < n2:
        sidi_lst.append(n1)
        sidi_lst.append(n2)
        return [n1, n2]
    else:
        sidi_lst.append(n1)
        sidi_lst.append(n2)
        return [n2, n1]


for i in range(1, 11):
    snake_dict[f"snake_{i}"] = genrate_rondom_snake()


for i in range(1, 11):
    sidi_dict[f"sidi_{i}"] = genrate_rondom_sidi()

for i in range(1, 11):
    main_lst[snake_dict[f"snake_{i}"][0]]["trap"] = snake_dict[f"snake_{i}"]

for i in range(1, 11):
    main_lst[sidi_dict[f"sidi_{i}"][0]]["trap"] = sidi_dict[f"sidi_{i}"]

player_dict = {
    1: {
        "color": "R",
        "is_completed": False,
        "is_started": False,
        "current_position": 1,
    },
    2: {
        "color": "B",
        "is_started": False,
        "is_completed": False,
        "current_position": 1,
    },
    3: {
        "color": "G",
        "is_started": False,
        "is_completed": False,
        "current_position": 1,
    },
    4: {
        "color": "Y",
        "is_started": False,
        "is_completed": False,
        "current_position": 1,
    },
}


# def check_token_outside(id):
# lst = []
# if id == 1:
#     if player_dict[id]["is_started"] == True:
#         lst.append("R1")
# elif id == 2:
#     if player_dict[2]["is_started"] == True:
#         lst.append("R2")
# elif id == 3:
#     if player_dict[3]["is_started"] == True:
#         lst.append("R3")
# elif id == 4:
#     if player_dict[4]["is_started"] == True:
#         lst.append("R4")

# return lst


def move_token(id, num):
    pos = player_dict[id]["current_position"]
    if pos + num <= 100:

        player_dict[id]["current_position"] = pos + num

        if main_lst[pos + num]["trap"] != "":
            player_dict[id]["current_position"] = main_lst[pos + num]["trap"][1]
            if main_lst[pos + num]["tokens"] == "":
                main_lst[main_lst[pos + num]["trap"][1]]["tokens"] = player_dict[id][
                    "color"
                ]
            else:
                main_lst[pos + num]["tokens"] = (
                    main_lst[main_lst[pos + num]["trap"][1]]["tokens"]
                    + ","
                    + player_dict[id]["color"]
                )
        elif main_lst[pos + num]["tokens"] == "":
            main_lst[pos + num]["tokens"] = player_dict[id]["color"]
        else:
            main_lst[pos + num]["tokens"] = (
                main_lst[pos + num]["tokens"] + "," + player_dict[id]["color"]
            )
        lst = main_lst[pos]["tokens"].split(",")
        index = lst.index(player_dict[id]["color"])
        lst.remove(lst[index])
        main_lst[pos]["tokens"] = (",").join(lst)
        if player_dict[id]["current_position"] == 100:
            player_dict[id]["is_completed"] = True
        else:
            return
    else:
        return


def check_user(id, num):
    if num == 6 and player_dict[id]["is_started"] == False:
        player_dict[id]["is_started"] = True
    elif player_dict[id]["is_started"] == True:
        move_token(id, num)
    else:
        return


def start_snake_and_ladder(length):
    for i in range(1, length + 1):

        if main_lst[1]["tokens"] == "":
            main_lst[1]["tokens"] = player_dict[i]["color"]
        else:
            main_lst[1]["tokens"] = (
                main_lst[1]["tokens"] + "," + player_dict[i]["color"]
            )
        print(i, ":", player_dict[i]["color"])
    # print(main_lst)
    print_snake_ladder()

    for i in count(0):
        for id in range(1, length + 1):
            counter = 0
            for i in count(0):
                if player_dict[id]["is_completed"] == False:
                    print(f"Turn of pleyer {id} : ")
                    num = int(input("enter digit : "))
                    # input(f"press any key : ")
                    # num = random_number()

                    if counter == 2 and num == 6:
                        continue
                    elif num == 6:
                        print("\nyou got :", num, "\n")
                        check_user(id, num)
                        print_snake_ladder()

                        counter = counter + 1
                    else:
                        print("\nyou got :", num, "\n")
                        check_user(id, num)
                        print_snake_ladder()

                        break
                else:
                    break


def display_menu():
    for i in count(0):
        try:
            print(
                "============================select pleyers============================"
            )
            print("1:   2 player")
            print("2 :  3 player")
            print("3 :  4 player")
            print("4 :    exit")
            print(
                "========================================================================================"
            )
            operations = int(input("Select any one option from upper list :").strip())

            if operations == 1:
                start_snake_and_ladder(2)
            elif operations == 2:
                start_snake_and_ladder(3)
            elif operations == 3:
                start_snake_and_ladder(4)

            elif operations == 4:
                print("Thank You For Visiting ludo game.....")
                break
            else:
                print("ERORR : Choice is Invalid....................")
        except Exception as err:
            print(err)
            continue


for i in count(0):
    try:
        print(
            "============================Welcome To Snake and ladder============================"
        )
        print("1:   start game")
        print("2 :  Exit")
        print(
            "========================================================================================"
        )
        operations = int(input("Select any one option from upper list :").strip())

        if operations == 1:
            display_menu()

        elif operations == 2:
            print("Thank You For Visiting snake and ladder game.....")
            break
        else:
            print("ERORR : Choice is Invalid....................")
    except Exception as err:
        print(err)
        continue
