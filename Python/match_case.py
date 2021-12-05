num = input("Enter numbers from 0 to 1:- ")
match num:
    case "0":
        print('You pressed zero')
    case '1':
        print('You pressed one')
    case _:
        print('Type the number dummy!!')
