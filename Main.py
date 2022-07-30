class Evaluate:class Evaluate:
  """This class validates and evaluate postfix expression.
  """This class validates and evaluate postfix expression.
  Attributes:
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
      stack: A List which acts as a Stack.
  """
  """
    # Write your code here
    # Write your code here




  def _init_(self, size):
  def _init_(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
    Arguments:
      size_of_stack: An integer to set the size of stack.
      size_of_stack: An integer to set the size of stack.
    """
    """
    self.top = -1
    self.top = -1
    self.size = size
    self.size = size
    self.lst = [None]*size
    self.lst = [None]*size




  def isEmpty(self):
  def isEmpty(self):
    """
    """
    Check whether the stack is empty.
    Check whether the stack is empty.
    Returns:
    Returns:
      True if it is empty, else returns False.
      True if it is empty, else returns False.
    """
    """
    # Write your code here
    # Write your code here
    if self.top == -1:
    if self.top == -1:
       return 1
       return 1
    else :
    else :
       return 0
       return 0
    
    
  def is_full(self):
  def is_full(self):
    # Write code here
    # Write code here
    if self.top == (self.size - 1):
    if self.top == (self.size - 1):
      return 1
      return 1
    else :
    else :
      return 0
      return 0
    
    
  def pop(self):
  def pop(self):
    """
    """
    Do pop operation if the stack is not empty.
    Do pop operation if the stack is not empty.
    Returns:
    Returns:
      The data which is popped out if the stack is not empty.
      The data which is popped out if the stack is not empty.
    """
    """
    # Write your code here
    # Write your code here
    if not self.isEmpty():
    if not self.isEmpty():
      z=self.lst[self.top]
      z=self.lst[self.top]
      del self.lst[self.top]
      del self.lst[self.top]
      self.top-=1
      self.top-=1
      return z
      return z


  def push(self, operand):
  def push(self, operand):
    """
    """
    Push the operand to stack if the stack is not full.
    Push the operand to stack if the stack is not full.
    Arguments:
    Arguments:
      operand: The operand to be pushed.
      operand: The operand to be pushed.
    """
    """
    # Write your code here
    # Write your code here
    if not self.is_full():
    if not self.is_full():
      self.top+=1
      self.top+=1
      self.lst[self.top]=operand
      self.lst[self.top]=operand




  def validate_postfix_expression(self, expression):
  def validate_postfix_expression(self, expression):
    """
    """
    Check whether the expression is a valid postfix expression.
    Check whether the expression is a valid postfix expression.
    Arguments:
    Arguments:
      expression: A String which represents the expression to be validated.
      expression: A String which represents the expression to be validated.
    Returns:
    Returns:
      True if the expression is valid, else returns False.
      True if the expression is valid, else returns False.
    """
    """
    # Write your code here
    # Write your code here
    count_1=0
    count_1=0
    count_2=0
    count_2=0
    for i in expression:
    for i in expression:
      if i.isdigit():
      if i.isdigit():
        count_1+=1
        count_1+=1
      else:
      else:
        count_2+=1
        count_2+=1
    if count_1>count_2 and expression[0].isdigit() and expression[1].isdigit():
    if count_1>count_2 and expression[0].isdigit() and expression[1].isdigit():
      return 1
      return 1
    else:
    else:
      return 1
      return 1




  def evaluate_postfix_expression(self, expression):
  def evaluate_postfix_expression(self, expression):
    """
    """
    Evaluate the postfix expression
    Evaluate the postfix expression
    Arguments:
    Arguments:
      expression: A String which represents the the expression to be evaluated
      expression: A String which represents the the expression to be evaluated
    Returns:
    Returns:
      The result of evaluated postfix expression.
      The result of evaluated postfix expression.
    """
    """
    # Write your code here
    # Write your code here
    for i in expression:
    for i in expression:
      if i.isdigit():
      if i.isdigit():
        self.push(i)
        self.push(i)
      else:
      else:
        var_1 = self.pop()
        var_1 = self.pop()
        var_2 = self.pop()
        var_2 = self.pop()
        if i=='/':
        if i=='/':
          self.push(str(eval(var_2 + i*2 + var_1)))
          self.push(str(eval(var_2 + i*2 + var_1)))
        else:
        else:
          self.push(str(eval(var_2 + i + var_1)))
          self.push(str(eval(var_2 + i + var_1)))
    return self.pop()
    return self.pop()




# Do not change the following code
# Do not change the following code
postfix_expression = input()  # Read postfix expression
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
    print(evaluate.evaluate_postfix_expression(tokens))
else:
else:
    print('Invalid postfix expression')
    print('Invalid postfix expression')
