# file: tb_sc/ch_09_unit_testing/sc_09_01_calculate.py
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    else:
        return None
