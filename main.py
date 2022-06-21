import lab2_2
import lab2_5
import lab2_5_part02
import lab2_7
import lab2_8
import lab2_8_part02
import lab2_8_part03
import lab2_8_part04
import lab2_9

def menu():
    while True:
        showMenu()
        option = input(">_")

        match int(option):
            case 1:
                lab2_2.exec()
                break
            case 2:
                lab2_5.exec()
                break
            case 3:
                lab2_5_part02.exec()
                break
            case 4:
                lab2_7.exec()
                break
            case 5:
                lab2_8.exec()
                break
            case 6:
                lab2_8_part02.exec()
                break
            case 7:
                lab2_8_part03.exec()
                break
            case 8:
                lab2_8_part04.exec()
                break
            case 9:
                lab2_9.exec()
                break

        if int(option) == 0:
            break

def showMenu():
    print("(1) - Lab 2.2")
    print("(2) - Lab 2.5")
    print("(3) - Lab 2.5 Part 02")
    print("(4) - Lab 2.7")
    print("(5) - Lab 2.8")
    print("(6) - Lab 2.8 Part 02")
    print("(7) - Lab 2.8 Part 03")
    print("(8) - Lab 2.8 Part 04")
    print("(9) - Lab 2.9")


if __name__ == '__main__':
    menu()


