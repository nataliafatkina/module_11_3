from inspect import getmodule
import inspect


def introspection_info(obj):
    result = {}

    # Определение типа объекта
    result['type'] = type(obj).__name__

    # Определение атрибутов объекта
    try:
        attr = [attr for attr in inspect.getmembers(obj, lambda x: not callable(x))
                                if not '__' in attr[0]]
        result['attributes'] = [item[0] for item in attr]
    except:
        result['attributes'] = []

    # Определение методов объекта
    meth = [attr for attr in inspect.getmembers(obj, lambda x: callable(x))
                                                                            if not 'class' in attr[0]]
    result['methods'] = [item[0] for item in meth]

    # Определение модуля объекта
    try:
        result['module'] = getmodule(obj).__name__
    except:
        result['module'] = obj.__class__.__module__

    return result


class Test:
    attr_1 = 0

    def __init__(self, name):
        self.name = name
        self.attr_2 = 1

    def test_run(self):
        return print('This is test')


def sum_(x, n):
    sum_ = 0
    for i in range(x):
        sum_ += n
    return sum_


number_info = introspection_info(42)
print(number_info)


t = Test('Nata')
number_info = introspection_info(t)
print(number_info)

number_info = introspection_info(Test)
print(number_info)

number_info = introspection_info(Test.test_run)
print(number_info)

number_info = introspection_info(sum_)
print(number_info)