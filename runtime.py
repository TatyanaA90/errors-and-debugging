def get_3rd_value(my_list):
    #Add conditional to return None if my_list has fewer than 3 items
    if len(my_list) < 3:
        return None
    return my_list[2]

def test_get_3rd_value():
    assert get_3rd_value([0, 1, 2]) == 2
    assert get_3rd_value([0, 1]) == None

def get_last_value(my_list):
    #Return None if the list is empty
    if not my_list:
        return None
    # Because lists use zero-indexing, the last index will always be len-1
    item_count = len(my_list) - 1
    return my_list[item_count]

def test_get_last_value():
    assert get_last_value([0, 1, 2]) == 2
    assert get_last_value([0]) == 0
    assert get_last_value([]) == None

def runtime_errors():
    test_get_3rd_value()
    test_get_last_value()

