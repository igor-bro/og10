# Управление элементами списка.

def add_element(main_list, x):
    main_list.append(x)
    return main_list


def delete_element(main_list):
    main_list.pop()
    return main_list


main_list = ["a","b","c","d"]
print("Главный список: ", main_list)
print("Список без последнего элемента: ")
print(delete_element(main_list))
x = str(input("Введите новый элемент:"))
print(add_element(main_list, x))
