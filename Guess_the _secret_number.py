print("Dear customer! Welcome to Guess the Secret Number Game! ")
start = input("Please press enter to continue")
secret = "2"
guess = input("Guess the secret number 'it is a whole number from 1-10': ")
if guess == secret:
        print("Congratulations! You have found the right number.")
else:
        print("Sorry your answer is incorrect!")
