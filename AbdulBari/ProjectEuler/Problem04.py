#A palindromic number reads the same both ways. The largest palindrom made from
#the product of two 2-digit numbers is 9009 = 91*99

#A * B = Palindrom  A 3-digit B 3-digit




def is_palindrome(number):
    string_number = str(number)
    reversed_string_number = string_number[::-1]
    return string_number == reversed_string_number

def largest_palindrome_product():
    largest_palindrome = 0
    # Begin multiplying numbers from 999
    for a in range(999, 99, -1):
        #for every a multiplying 999 to 100
        for b in range(999, 99, -1):
            #The current_product 
            current_product = a * b
            # If the current number is polindrom and current_number bigger than latest and largest palindrome.
            if is_palindrome(current_product) and current_product > largest_palindrome:
                largest_palindrome = current_product
                print(a,b)
    return largest_palindrome
    
largest_palindrome = (largest_palindrome_product())
print("The biggest polindrom made by the product of 3 digit is :{} ".format(largest_palindrome))
