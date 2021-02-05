def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec



def func_to_be_executed():
    print("No pain NO gain")

func_to_be_executed = dec1(func_to_be_executed)

func_to_be_executed()
