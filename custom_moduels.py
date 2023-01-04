import my_module
from my_module import sum_calc as sc

print(my_module.test_var)

my_module.test_function(123)

test = my_module.Test()
test.do_something()

sc(2,3,4,7)

print(__name__)

if __name__ == '__main__':
    print('the main file')