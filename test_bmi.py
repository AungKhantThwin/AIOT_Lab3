import AIOT_Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.7, 30)
    test_result = -1
    assert (result == test_result)
    

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.7, 65)
    test_result = 0
    assert (result == test_result)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.7, 100)
    test_result = 1
    assert (result == test_result)

