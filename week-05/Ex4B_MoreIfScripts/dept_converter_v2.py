
depart_code = int(input("depatment number"))

match depart_code:
    case 1:
        print("marketing")

    case 5:
        print("human resources")

    case 10:
        print("accounting")

    case 12:
        print("legal")

    case 18:
        print("IT")

    case 20: 
        print("customer relations")

    case other:
        print("not found")