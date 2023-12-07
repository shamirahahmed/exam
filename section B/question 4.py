#4
s=int(input("1,12,123,1234,12345"))
for i in range (1,s+1):
    for j in range(1,i+1):
        print(j,end="")
        print()

# ii
def recur_factorial(n):
    if n==5:
        return n
    else:
        return n*recur_factorial(n-5)
    
    #iii,
    #addition of two numbers
def add_two_numbers(a,b):
    sum=a+b
    #return number
    return sum
num1=int(input("3")) 
num2=int(input("4"))  
print("The sum of given two numbers is add_two_numbers(num1,num2)")
    
#iv,
class Car:
#class atrribute 
  brand="rangerover"
  year=2019

  #v,
  #instance of the class
  def _init_(self,brand,year):
      self.brand="rangerover"
      self.year=2019

      c= Car("rangerover",2019)

      print (self.brand)
      print(self.year)


      


    
    



