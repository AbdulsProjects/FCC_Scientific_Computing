def arithmetic_arranger(*args):
    #Assigns the list of problems into a variable
    problems = args[0]
    arranged_problems = ""
    
    
    #Returns an error if there are * or / operators
    for problem in problems:
        if ("*" in problem or "/" in problem):
            return "Error: Operator must be '+' or '-'."
    
    
    #Returns an error if more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."    
        
        
    #Splits each problem into 3 elements
    for i in range(len(problems)):
        problems[i] = problems[i].split(" ")


    #For loop that raises errors  
    for i in range(len(problems)):
        
        #Raises an error if any characters within operons arn't numeric
        if problems[i][0].isnumeric() == 0 or problems[i][2].isnumeric() ==0:
            return "Error: Numbers must only contain digits."
        
        #Raises an error if any of the operons are more than 4 characters long 
        if len(problems[i][0]) > 4 or len(problems[i][2]) > 4:
            return "Error: Numbers cannot be more than four digits."
           
            
    
    #Code used to display the operations
    
    #Calculating length of largest operon for each problem
    largest_list = []
    for i in range(len(problems)):
        if len(problems[i][0]) > len(problems[i][2]):
            largest_list.append((len(problems[i][0]), 1))
        else:
            largest_list.append((len(problems[i][2]), 2))
        
    #First line
    for i in range(len(problems)):
        #Calculates how many spaces are needed between operator and number, then inserts them.
        for size in range(largest_list[i][0] + 2 - len(problems[i][0])):
            arranged_problems += ' '

        #Used to add every number except for the last to the 1st line        
        if i < (len(problems) - 1):
            arranged_problems += problems[i][0] + '    '
        
        #Adds last number to 1st line
        else:
            arranged_problems += (problems[i][0] + '\n')

    
    #Second line
    for i in range(len(problems)):
        #Adds operator
        arranged_problems += problems[i][1] + ' '
        #Calculates how many spaces are needed between operator and number, then inserts them.
        for size in range(largest_list[i][0] - len(problems[i][2])):
            arranged_problems += ' '
        
        #Used to add every number except for the last to the 2nd line
        if i < (len(problems) - 1):
            arranged_problems += (problems[i][2] + '    ')  
        
        #Adds last number to 2nd line
        else:
            arranged_problems += (problems[i][2] + '\n')

    
    
    #Dashes
    for i in range(len(problems)):
        for x in range(largest_list[i][0] + 2):
            arranged_problems += '-'
        
        #Adds spaces if there are more equations
        if i < (len(problems) - 1):
            arranged_problems += '    '  
    
    
   #Prints the answer if 2nd arguement is "True"
    if args[-1] == True:
        arranged_problems += '\n'
        for i in range(len(problems)):
            
            #Addition
            if problems[i][1] == "+":
                answer = int(problems[i][0]) + int(problems[i][2])
                
            #Subtraction
            elif problems[i][1] == "-":
                answer = int(problems[i][0]) - int(problems[i][2])
            
            #ValueError due to incorrect operator
            else:
                raise ValueError(F"{problems[i][1]} isn't an accepted operator.")
              
            #Print answer
            for size in range(largest_list[i][0] + 2 - len(str(answer))):
                arranged_problems += ' '
            
            #Adds space if it's not the last answer
            if i < (len(problems) - 1):
                arranged_problems += str(answer) + '    '
            
            else:
                arranged_problems += str(answer)

    return arranged_problems
