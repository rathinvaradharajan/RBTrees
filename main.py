from RBTree import RBTree


def main():
    tree = RBTree()

    with open("input.txt", "r") as f:
        line = f.readline()
        while line:
            for value in line.split():
                tree.insert(int(value))
                print("Height: ", tree.height())
            line = f.readline()
    print(tree.sort())
    value = ""
    while value != "\\q":
        print("\nEnter Command:\n1. Insert X\n2. Search X"
              "\n3. Min\n4. Max\n5. Successor X\n6. Predecessor X\n7. Sort\n8. Height\n Press \\q to quit")
        value = input()
        command = value.split()[0]
        if command == "Insert" or command == "insert":
            tree.insert(int(value.split()[1]))
            print("Height: ", tree.height())
        elif command == "Search" or command == "search":
            print("Search ", value.split()[1], ": ", tree.search(int(value.split()[1])))
        elif command == "Min" or command == "min":
            print("Min: ", tree.min())
        elif command == "Max" or command == "max":
            print("Max: ", tree.max())
        elif command == "Successor" or command == "successor":
            print("Successor: ", tree.successor(int(value.split()[1])))
        elif command == "Predecessor" or command == "predecessor":
            print("Predecessor: ", tree.predecessor(int(value.split()[1])))
        elif command == "Sort" or command == "sort":
            print("Sort: ", tree.sort())
        elif command == "Height" or command == "height":
            print("Height: ", tree.height())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
