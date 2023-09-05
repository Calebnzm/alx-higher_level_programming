#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    division_result = my_list_1[i] / my_list_2[i]
                    result.append(division_result)
            else:
                result.append(0)
                print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            pass
    return result
