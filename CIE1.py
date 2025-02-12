x = 10
def my_function():
   y = 5

   global x
   x = 20

   print("Inside a function:")
   print("Global variable x:" ,x)
   print("local variable y:",y)

my_function()

print("Outside function:")
print("Global variable x:", x)
