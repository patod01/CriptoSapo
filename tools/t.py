from franky import make_format_time

# print(make_format_time.__doc__)

# make_format_time test
print(make_format_time('1661049936.8458757') == '2022-08-20 22:45')
print(make_format_time('1661049936.8458757', seconds=True) == '2022-08-20 22:45:36')
print(make_format_time.__doc__)
