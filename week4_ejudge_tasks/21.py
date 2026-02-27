import importlib

command_n = int(input())
for i in range(command_n):
    m_path, attribute = map(str, input().split())
    try:
        module = importlib.import_module(m_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    if hasattr(module, attribute):
        if callable(getattr(module, attribute)):
            print("CALLABLE")
        else:
            print("VALUE")
    else:
        print("ATTRIBUTE_NOT_FOUND")
    