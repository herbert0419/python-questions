#User will input (3ages).Find the oldest one



age1 = input('Enter the age1:')
age2 = input('Enter the age2:')
age3 = input('Enter the age3:')


#using max() built-in function

oldest = max(age1,age2,age3)
print("The oldest one is:",oldest)

youngest = min(age1,age2,age3)
print("The oldest one is:",youngest)

#using chained if-else

if age1>=age2 and age1>=age3:
    oldest_age = age1
elif age2>=age1 and age2>=age3:
    oldest_age = age2
else:
    oldest_age = age3

print(oldest_age, "is the oldest one")

# using nested if-else:

if age1>=age2:
    temp_age = age1
else:
    temp_age = age2

if temp_age>=age3:
    oldest_age = temp_age
else:
    oldest_age = age3

print(oldest_age, "is the oldest one.")





