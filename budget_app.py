
class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.catBalance = 0
    
    def __str__(self):  
        label = "{:*^30s}".format(f"{self.category}") + "\n"
        for x in self.ledger:
            label += f"{x['description'][:23].ljust(23)}"+ "{:.2f}".format(x['amount']).rjust(7) + "\n"
        total = self.get_balance()
        label += "Total: " + "{:.2f}".format(total)
        return label

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': float(amount), 'description' : description})
        self.catBalance += amount
       
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({'amount': float(-amount),'description': description})
            self.catBalance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.catBalance
        
    def transfer(self, amount, destination):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to [Destination Budget Category]")
            return True
        else:
            return False
           
          
    def check_funds(self, amount):
        if amount <= self.catBalance:
            return True
        else:
            return False
       

def create_spend_chart(categories):
  catNames = []
  spent = []
  spentPct = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total = total- item['amount']
    spent.append(round(total, 2))
    catNames.append(category.category)

  for amount in spent:
    spentPct.append(round(amount / sum(spent), 2)*100)

  barChart = "Percentage spent by category\n"

  yAxis = range(100, -10, -10)

  for label in yAxis:
    barChart += str(label).rjust(3) + "| "
    for pct in spentPercentages:
      if pct >= label:
        barChart += "o  "
      else:
        barChart += "   "
    barChart += "\n"

  barChart += "    ----" + ("---" * (len(catNames) - 1))
  barChart += "\n     "

  maxLength = 0
  for n in catNames:
    if maxLength < len(n):
      maxLength = len(n)

  for i in range(maxLength):
    for n in catNames:
      if len(n) > i:
        barChart += n[i] + "  "
      else:
        barChart += "   "
    if i < maxLength - 1:
      barChart += "\n     "

  return(barChart)




"""
Assignment

Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. 
When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list.

The class should also contain the following methods:

    [OK] - A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. 
    The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.

    [OK] - A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. 
    If there are not enough funds, nothing should be added to the ledger. 
    his method should return True if the withdrawal took place, and False otherwise.
    
    [OK] - A get_balance method that returns the current balance of the budget category 
    based on the deposits and withdrawals that have occurred.

    [OK] - A transfer method that accepts an amount and another budget category as arguments. 
    The method should add a withdrawal with the amount and the 
    description "Transfer to [Destination Budget Category]". 
    The method should then add a deposit to the other budget category with the amount and 
    the description "Transfer from [Source Budget Category]". If there are not enough funds, 
    nothing should be added to either ledgers. 
    This method should return True if the transfer took place, and False otherwise.

    [OK] - A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the
    balance of the budget category and returns True otherwise. This method should be used by both the withdraw method 
    and transfer method.

[OK] When the budget object is printed it should display:

    A title line of 30 characters where the name of the category is centered in a line of * characters.
    A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, 
    then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    A line displaying the category total.

Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Besides the Category class, create a function (ouside of the class) called create_spend_chart that takes a list of categories as an argument. 
It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with 
withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of 
the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past 
the final bar. Each category name should be vertacally below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

"""