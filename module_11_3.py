import requests


def introspection_info(obj):
    result = {}

    result['type'] = type(obj)

    try:
        result['attributes'] = getattr(introspection_info, obj)
    except:
        result['attributes'] = []

    result['methods'] = dir(obj)
    result['module'] = obj.__class__.__module__

    return print(result)

number_info = introspection_info(42)
print(number_info)