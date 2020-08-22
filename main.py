# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def open_file(path):
    new_file = open(path, "r+")
    return new_file


def close_file(file_name):
    file_name.close()


def count_letters():
    new_dict = dict()
    new_file = open_file("test.txt")
    for line in new_file.readlines():
        for letter in line:
            new_dict[letter] = new_dict.get(letter, 0) + 1
    sorted_dict= sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    for k,v in sorted_dict:
        if k != '\n':
            print("'", k, "'", " appears ", v, " times ", sep="")
    close_file(new_file)

def count_words():
    new_dict = dict()
    new_file = open_file("test.txt")
    for line in new_file.readlines():
        for word in line.split():
            new_dict[word] = new_dict.get(word,0) + 1
    sorted_dict = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    for k,v in sorted_dict:
        print("'", k, "'", " appears ", v, " times ", sep="")
    close_file(new_file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\nCount Words:")
    count_words()
    print("\nCount Letters:")
    count_letters()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
