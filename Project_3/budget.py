class Category:
    
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.balance = 0.0
        #Variables used to track how much spent, used for the graph
        self.spent = 0.0


      
    def deposit(self, amount, description = ""):
        #Adds deposited amount and description to ledger        
        self.ledger.append({"amount": amount, "description": description})
        #Adds deposit to balance
        self.balance += amount

               
    
    def withdraw(self, amount, description = ""):
        #Checks if there are sufficient funds
        if self.check_funds(amount):
            #Adds withdrawed amount and description to ledger
            self.ledger.append({"amount": -amount,"description": description})
            #Subtracts amount from balance
            self.balance -= amount
            self.spent += amount
            return True
        #Insufficient funds
        else:
            return False
        
      
    def get_balance(self):
        return self.balance
        

    def transfer(self, amount, sink):
        #Sufficient funds
        if self.check_funds(amount):
            #Withdraws from source
            self.withdraw(amount, f"Transfer to {sink.name}")
            #Deposits into self
            sink.deposit(amount, f"Transfer from {self.name}")
            return True
        #Insufficient funds
        else:
            return False
        
        
    def check_funds(self, amount):
        #Enough funds
        if amount <= self.balance:
            return True
        #Not enough funds
        else:
            return False


    #Formatting the object print value
    def __str__(self):
       #Create output, and add first line
       output = self.name.center(30, '*')
       #Adds the ledger to the output, line by line
       for i in range(len(self.ledger)):
           
           #Adds the description of the current entry
           output += "\n" + self.ledger[i]['description'][0:23].ljust(23)

           #Adds the amount of the current entry
           output_num = "{:.2f}".format(self.ledger[i]['amount'])
           output += str(output_num)[0:7].rjust(7)
       
       #Adds total to output
       output += "\nTotal: " + str(self.balance)
       return output


def create_spend_chart(catagories): 
    catagory_names = []
    total_spent = 0.0
    spent_percent_list = []
    
    
    #Assigning catagory names
    for catagory in catagories:
        catagory_names.append(catagory.name)
        #Calculating total spent
        total_spent += catagory.spent
       

    #Finding length of longest name (needed for output x-axis labels)
    longest_name_len = len(catagory_names[1])
    
    for i in range(len(catagory_names)):
        if len(catagory_names[i]) > longest_name_len:
            longest_name_len = len(catagory_names[i])

       
    #Calculating spent percentage
    for catagory in catagories:
        #Calculating percent
        spent_percent = (catagory.spent / total_spent) * 100
        #Rounding percentage down to nearest 10
        spent_percent = int(spent_percent / 10) * 10
        #Storing percentage value
        spent_percent_list.append(spent_percent) 

    
    #Creating graph
    #Header
    chart = 'Percentage spent by category'
    
    #Vertical axis and values (unformated for spaces after values)
    for i in range(100, -10, -10):
        #Creating axis labels
        if i == 100:
            chart += '\n' + str(i) + '|'
        #Adds 2 spaces before axis label for 0 row
        elif i == 0:
            chart += '\n  ' + str(i) + '|'
        #Adds 1 space before axis label if  100 > x >= 10
        else:
            chart += '\n ' + str(i) + '|'
        #Adding in axis values
        for key in spent_percent_list:
            if key >= i:
                chart += ' o '
            else: 
                chart += '   '
               
    #Creating the x axis
    chart += '\n    '
    #Calculating axis line length
    axis_length = 5

    #Adding the dashes
    for i in range(len(catagories)):
        chart += '---'
        axis_length += 3
    chart += '-'

    #Formatting the graph above the x axis
    split_chart = chart.splitlines()
    for i in range(len(split_chart)):
        #Identifying which lines need spaces
        if len(split_chart[i]) < axis_length:
            split_chart[i] = split_chart[i].ljust(axis_length)
    #Rejoining split lines
    chart = ('\n'.join(split_chart))
    


    #Adding the catagory labels
    for i in range(longest_name_len):
        chart += '\n    '
        for key in catagory_names:
            if len(key) >= (i + 1):
                chart += ' ' + key[i] +' '
            else:
                chart += '   '
        chart += ' '
        
    return chart
