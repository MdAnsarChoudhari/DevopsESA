from number import check_number


def test_check_number():

    assert check_number(6)==["the number is even", "the number is not prime"]