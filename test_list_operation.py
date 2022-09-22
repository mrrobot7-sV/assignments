import pytest
import list_operation


# TESTCASES
# ========================================== #

# test cases for list_operation (List Operation)
def test_list_operation():
    assert(list_operation.list_operation(1, 10, 3) == [3, 6, 9])
    assert(list_operation.list_operation(7, 9, 2) == [8])
    assert(list_operation.list_operation(15, 20, 7) == [])
    assert(list_operation.list_operation(15, 21, 7) == [21])
    with pytest.raises(ValueError):
        list_operation.list_operation(22, 21, 7)