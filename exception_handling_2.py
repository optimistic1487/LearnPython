#Day 10
#EXCEPTION HANDLING
#Understanding of Exception: what, exception handler blocks (try,except,else,finally)
#Exception handling methodologies: Block level or Statement level
#Types of Exception: Predefined (TypeError, ValueError, KeyError,DivideByZero,IndexError,FileNotFound..) & Userdefined/CustomExceptions
#importance - Dataengineer less (already framework spark or any other handled the exceptions)
#importance - python developer (application/framework/tool/automation) medium (already framework spark handled the exceptions)
#What? - Exception is a error occurrs when the program is executing at any stage for any
# reasons (data error, name/key/value error, type error, environment error, file not found, format error)
# and makes the flow of program terminated abruptly (out of control)
# Exception Handler (graceful handling of program termination by generating logs, messages, alternative codes, releasing of resources, closing of connections)
# help us handle or take the control from the line where main program got terminated - is a construct/code that help us handle the state of exception
#Example:
#exception->exceptional cases, unexpected events, unusual, abnormal..
#1. try - I am going to a store to buy something to my home (plan it perfectly to avoid any unexpected events)
    #take a vehicle
    # go to shop,
    # add different items in the cart,
    # pay the bill,
    # take a vehicle
    # come back home
#2. except - any unexpected event occurs, handle it accordingly
    #exception1 - trip got cancelled because of some other priority work came
    #exception2 - vehicle is not starting, but i may use some other vehicle or go by walk or call the mechanic and abort my journey
    #exception3 - shop is closed
    #exception4 - some products are not available...
    #exp5- card declined/not accepted or wallet is lost
    #exp6 - vehicle is not starting
    #exp7 - something went wrong which i didn't predicted (expect unexpected)
#3. else - (If except doesn't happened) If I am not getting any exception, what I have to do then?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
#4. finally (If 1+3 or 2  happened) If I am not getting any exception or I got some exception, what I have to do?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
    #plan for some other alternative journey
#1 and 2 are mandatory
try:
    print("try is mandatory")
except Exception as msg:
    print(msg)
#3 and 4 are not mandatory
try:
    print("try is mandatory")
except Exception as msg:
    print(msg)
else:
    print("prog completed success - optional")
finally:
    print("Eigther prog completed success or Exception may occured - optional")

#############################################################################################
print("Example 1 - Intro to Exception handling - to understand what, why, when, blocks/constructs of exception handler in python")
try:
    sal=int(input("Enter the salary\n")) # if anything goes wrong, the exit(1) will occur
    bon_pct=10
    den = int(input("Enter the denominator\n"))
    final_sal=sal+(sal*(10/den)) #;exit(1)
    print(f"Main program - bonus applied sal is {final_sal}")
    #print("bonus given for this month is "+bon_pct)

except ValueError as err_msg:
    print("ValueError - Rather than abruptly aborting the program, I am going to take the control in the exception handler block")
    print(f"Enter the salary in a int format for eg. 10000 or 20000 like that and retry - Actual Err message is : {err_msg}")
except ZeroDivisionError as err_msg:
    print("ZeroDivisionError - Rather than abruptly aborting the program, I am going to take the control in the exception handler block and apply some alternative solution")
    print(f"Zero division error have occured, let the exception handler handles it gracefully  : {err_msg}")
    final_sal=sal+(sal*(10/100))
    print(f"Exception handler program -  bonus applied sal is {final_sal}")
except Exception as err_msg:
    print(f"Exception handler program -  Some unexpected exception occured, lets make some common arrangements {err_msg}")
else:
    print("Else Block - (TRY something if anything goes wrong goto EXCEPTION block else go to ELSE block) Else block in Exception handler program is called if no exception occurs when the main block runs")
    print("If main program complete success, then what I have to do, will be happening in the else block")
    #Close all the files I opened, clean the temporary files if the program complete successfully..
finally:
    print("Finally Block - (TRY something if anything goes wrong goto EXCEPTION block else go to ELSE block but go to FINALLY block whether you goto EXCEPTION or ELSE block)")
    print("At any cost whether Exception occurs or not, got to finally block finally - What ever happens finally runs")
    #Close all the files I opened, DB connections opened, clean the temporary files if the program complete successfully or failed..

#############################################################################################
#Day 11
print("Example 2 - Exception Handler Types (Predefined & Userdefined/Custom) + Different Types of Predefined Exceptions in exception handler in python")
print("Let's see about Predefined/Builtin Exception types - If already the Python has some regular exception classes/programs created and kept ready to use")
print("Eg. ValueError,ZeroDivisionError ")
print("Order of Exception classes we have to maintain, where subclassess has to be used first and then super classes has to used after subclassess")
print("Custom/User defined Exceptions - We can create our own exception handler class and call/raise exception as per the business requirement")
#Depends upon the program, logic, functions used - we have to use the necessary exception classes

#User Defined/Custom Exception Handler - Creation of an Exception handler class for a custom need
class InceptezCustomException(Exception):
    print("Exception occured due to wrong bonus pertage entered by the user")

try:
    #import json2#ModuleNotFound error
    # import json
    # openfile = open("/home/hduser/sparkdata/file1.json", 'r')
    # readjsonfile = json.load(openfile)
    # cols=readjsonfile['cols']
    sal=int(input("Enter the salary\n")) # if anything goes wrong, the exit(1) will occur
    bon_num=int(input("Enter the bonus value\n"))
    if bon_num>30:
        #raise Exception
        raise InceptezCustomException #We can call exeption handler program anytime when we needed
    den = int(input("Enter the denominator\n"))
    assert den==100,"denominator should be 100" #assertion (check) very important function to assert/validate/check something
    bonus_pct=(bon_num/den)
    #print(bonus_pct1)#NameError
    final_sal=sal+(sal*bonus_pct) #;exit(1)
    print(f"Main program - bonus applied sal is {final_sal}")
    #print("bonus given for this month is "+bon_pct)
    emp_list=["Bala","Akkalesh","Venu"]
    #print(emp_list[3])#IndexError
    emp_dict = {1:"Bala", 2:"Akkalesh", 3:"Venu"}
    #print(emp_dict[3])#KeyError
    #print("length of the final sal is ",len(final_sal))#TypeError
    print("length of the final sal is ", final_sal.append(" is the Final salary"))  # AttributeError

except InceptezCustomException as err_msg:
    print(f"Custom exception occured - {err_msg}")
    print("Sending mail to the management")
except ModuleNotFoundError as err_msg:
    print(f"imported module is not exits - {err_msg}")
except FileNotFoundError as err_msg:
    print(f"Given file is not exits - {err_msg}")
except TabError as err_msg:
    print(f"IndentationError - Tab and spaces are used wrongly - {err_msg}")
except IndentationError as err_msg:
    print(f"IndentationError - Indentation error occured - {err_msg}")

except NameError as err_msg:
    print(f"Variable name is not defined - {err_msg}")

except IndexError as err_msg:
    print(f"Index out of bound exception occured - {err_msg}")
except KeyError as err_msg:
    print(f"Key doesn't exist in the Dict - {err_msg}")

except TypeError as err_msg:
    print(f"Given data type doesn't support the len function  - {err_msg}")

except AttributeError as err_msg:
    print(f"Given data type doesn't extends/support the append attribute  - {err_msg}")

except ValueError as err_msg:
    print("ValueError - Rather than abruptly aborting the program, I am going to take the control in the exception handler block")
    print(f"Enter the salary in a int format for eg. 10000 or 20000 like that and retry - Actual Err message is : {err_msg}")

except AssertionError as err_msg:
    print(f"AssertionError - {err_msg}")

except ZeroDivisionError as err_msg:
    print("ZeroDivisionError - Rather than abruptly aborting the program, I am going to take the control in the exception handler block and apply some alternative solution")
    print(f"Zero division error have occured, let the exception handler handles it gracefully  : {err_msg}")
    final_sal=sal+(sal*(10/100))
    print(f"Exception handler program -  bonus applied sal is {final_sal}")
except ArithmeticError as err_msg:
    print("ArithmeticError - Some Arithmetic error occured")

except Exception as err_msg:
    print(f"Exception handler program -  Some unexpected exception occured, lets make some common arrangements {err_msg}")

print("Example 3 - Exception handling methodologies: Block level or Statement level")
try:
    print("Block Level Exception Handling")
    sal=10000
    bonus=10
    bonus_sal=sal+(sal*(bonus/0))
    len(bonus_sal)
except ZeroDivisionError as msg:
    print(f"zero division exception occured {msg}")
except TypeError as msg:
    print(f"Type error exception occured {msg}")
except Exception as msg:
    print(f"Some exception occured {msg}")

#############################################################################################
#Statement level exeception will be used if we want to handle exceptions at the statement level and not block level
#ie. if any exception occurs in one statement should not terminate the entire program despite it has to continue to the next statemnt
#If we still wanted few exceptions has to terminate the enter module/program, then we can use exit(1)
try:
    print("Statement Level Exception Handling (handle exception on every statements and not at the blok level)")
    print("Statement1")
    sal=10000
    bonus=10
    bonus_sal=sal+(sal*(bonus/0))
except ZeroDivisionError as msg:
    print(f"zero division exception occured {msg}")
except Exception as msg:
    print(f"Some exception occured {msg}")

try:
    print("Despite Statement1 fails, I still wanted to continue to Statement2")
    print("Executing second statement2")
    print(bonus_sal)

except TypeError as msg:
    print(f"Type error exception occured {msg}")
    exit(1)
except Exception as msg:
    print(f"Some exception occured {msg}")
    exit(2)

try:
    print("I dont wanted to continue statement3 if Statement2 fails")
    print("Executing third statement3")
    #print(len(bonus_sal))

except TypeError as msg:
    print(f"Type error exception occured {msg}")
except Exception as msg:
    print(f"Some exception occured {msg}")

#############################################################################################
