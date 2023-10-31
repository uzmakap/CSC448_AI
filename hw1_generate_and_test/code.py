# BY: UZMABANU KAPADIA 
# This function takes the number and checks to see if the given number is a prime or not
def is_a_prime(number):
    possible_factor = 2
    while possible_factor < number:
        if number % possible_factor == 0:
            return False  # given number is not prime
        possible_factor += 1
    return True  # given number is prime

# This tests the is_a_prime function for numbers between 3 and 100
for number in range(3, 101):
    if is_a_prime(number):
        print(number, "is prime")
    else:
        print(number, "is not prime")