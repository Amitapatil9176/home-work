def log_deco(func):
    def wrapper_fun():
        print(f"calling function ")
        func()
        print(f"finished function")
        return wrapper_fun()
@log_deco
def disp():
    print("hello world")
disp()
