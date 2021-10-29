import requests
import html
print("Welcome to the CSTrivia Quiz!")
try:
    name = input("What is your name? ")
    print("Hello, " + name + "!")
    questionNumber = input("How many questions would you like to answer?(1-10) ")
    print("You will be asked " + questionNumber + " questions.")
    difficulty = input("What difficulty would you like to play on? (easy, medium, hard) ")
except:
    print("Error: Invalid input.Try again.")
    exit()
print("You will be asked questions on " + difficulty + " difficulty.")
print("Please respond with True or False.")
print("Good luck!")

# This is the URL for the API
triviaURL = 'https://opentdb.com/api.php?amount=%s&category=18&difficulty=%s&type=boolean' % (questionNumber, difficulty.lower())

# OpenTDB API returns JSON data
response = requests.get(triviaURL).json()
score = 0
for i in range(0, int(questionNumber)):
    print(html.unescape(response['results'][i]['question']))
    answer = input("Answer: ")
    answer = answer.lower()
    correctAnswer = response['results'][i]['correct_answer']
    correctAnswer = correctAnswer.lower()
    if answer == correctAnswer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print("You scored " + str(score) + " out of " + questionNumber + "!")
print("Thanks "+ str(name) +" for playing!")