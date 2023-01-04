def test_function(content):
    print(f"This is an imported function with the parameter: {content}")


class Test:
    def __init__(self) -> None:
        self.name = 'My App'
        self.value = 12
    def do_something(self):
        print('Hello')

test_var = 'test'

def sum_calc(*numbers: int):
    print(sum(numbers))
    
if __name__ == '__main__':
    print(__name__)