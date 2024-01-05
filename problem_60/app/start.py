#Project Euler - Problem 60
#Solution by Lean
from sympy import isprime
primes = {'3':[[3]]}
n = 5

#search and add new remarkable couple
def is_remarkable_couple(n,m):
  nm = str(n) + str(m)
  mn = str(m) + str(n)
  if isprime(int(nm)) & isprime(int(mn)):
    #n and m are remarkables
    return True
  else:
    #n and m are not remarkables
    return False

#assume a very big sum number 
min_item_sum = 10e100

while True:
  #if n is prime
  if isprime(n):
    #make a list of remarkable lists with n
    list_of_new_items = [[n]]
    # for each prime (key) in primes
    for m in primes:
      #if n and m are remarkables
      if is_remarkable_couple(n,int(m)):
        #for each list of remarkables with m
        for item in primes[m]:
          new_item = []
          all_remarkables = True
          for number in item:
            if is_remarkable_couple(n,number):
              new_item.append(number)
            else:
              all_remarkables = False
              break              
          if all_remarkables:
            new_item.append(n)
            if len(new_item) == 5:
              if sum(new_item) < min_item_sum:
                min_item_sum = sum(new_item)
            list_of_new_items.append(new_item)
      else:
        #if n is not remarkable with the key, then test with next key
        continue
    #add new key in primes with its value, an empty list    
    primes[str(n)] = []
    #for each list in the temporary remarkable list
    for item in list_of_new_items:
      #append on the corresponding key
      primes[str(n)].append(item)
  n += 1
  #continue until n is bigger than the sum an then break 
  if n >= min_item_sum:
    break


print("minimum sum: ",min_item_sum)