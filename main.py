#Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number%i == 0:
      is_prime = False
  if is_prime:
    print("it's a prime number.")
  else:
    print("it's not a prime number.")
  # if number == 2:
  #   print("number is prime")
  # elif number == 3:
  #   print("number is prime")
  # elif number %2 == 0 or number %3 == 0:
  #   print("number is not prime")
  # else:
  #   print("number is prime")






#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



