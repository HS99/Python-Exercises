print('Break Example: Break when . occurs in the string')
for letter in 'The Quick Brown Fox. Jumps, Over The Lazy Dog':
   if letter == '.':
      break
   print ('Current Letter :', letter)
print('Continue Example')
for num in range(10, 21):
   if num % 5 == 0:
      print ("Found a multiple of 5")
      pass
      num = num + 1
      continue
   print ("Found number: ", num)
