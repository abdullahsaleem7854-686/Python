
def Sum(x,y):
    print(f'sum is {x + y}')


a = int (input("Enter value of a: "))
b = int(input("Enter value of b: "))
Sum(a,b)

def Avg(marks):
   sum = 0
   for i in marks:
       sum += i
   avg =  sum/len(marks)
   print(f'Average of marks {avg}')

marks = [23,50,69,79,97,99]
print(Avg(marks))





