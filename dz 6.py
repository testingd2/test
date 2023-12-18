result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більше або рівне b")
        if b > 100:
            raise IndexError("b має бути менше або рівне 100")
        if b == 0:
            raise ZeroDivisionError("b не може бути нулем")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except Exception as e:
        print(f"Exception: {e}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)