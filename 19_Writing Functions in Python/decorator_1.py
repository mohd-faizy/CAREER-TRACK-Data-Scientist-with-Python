def inner1(func): 
    def inner2():
        print("Before function execution"); 
        func() 
        print("After function execution")    
    return inner2 

@inner1
def function_to_be_used(): 
    print("This is inside the function") 

function_to_be_used()  