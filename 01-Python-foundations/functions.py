# functions

def user_input(env):
    if env == "dev" or env == "stg":
        print("you can deploy on friday")
    elif env == "prd":
        print("you can't deploy on friday")    
    else:
        print(" you can deploy on any day")    

# env = input("enter the environment : ")
# user_input(env) 