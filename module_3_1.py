calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string = str(string)
    tuple_ = (len(string),string.upper(),string.lower())
    count_calls()
    return tuple_
def is_contains(str_,list_):
    str_ = str(str_).lower()
    list_ = list(list_)
    count_calls()
    for i in range(len(list_)):
        if str(list_[i]).lower()== str_:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Copybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban','urBAN']))
print(is_contains('cycle',['cyclic','recycling']))
print(calls)
