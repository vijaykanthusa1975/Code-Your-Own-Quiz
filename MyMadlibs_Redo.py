import re
import string
import itertools
import time
import os

def exit_fn():
    """Function to exit program after waiting for 10 seconds
    Args:
        None
    Returns:
        None
    Raises:
        None
    """
    time.sleep(10) #wait for 10 seconds before close
    os._exit(1)#exit OS

def err_incorrect_Ans_counter(i,incorrect_Ans_counter,parts_of_speech):
    """Function to calculate number of incorrect tries
    Args:
        i: while loop incrementer variable from calling function
        parts_of_speech: Answers corresponding to blank values
        incorrect_Ans_counter: Counter to number of incorrect correct answers per quiz
    Returns:
        Incorrect counter value to calling function if more entries are allowed
    Raises:
        Number of tries remaining messaage
    """
    if i==len(parts_of_speech):#check if i has reached the length of list
        incorrect_Ans_counter=incorrect_Ans_counter-1 #decrement counter for last invalid input
        print "\nIncorrect. Tries remaining \t",incorrect_Ans_counter, "\nNo more tries allowed \n" #print incorrect_Ans_counter
        exit_fn() #Function to exit program
    else:
        incorrect_Ans_counter=incorrect_Ans_counter-1 #decrement counter for each invalid input
        print "\nIncorrect. Tries remaining \t", incorrect_Ans_counter #print incorrect_Ans_counter
        return incorrect_Ans_counter #Return counter if more entries are allowed

def play_Madlibs(test_string,blanks,parts_of_speech,correct_Ans_counter):
    """Function takes user input for test string, blank values, Answer values, correct_Ans_counter
    Args:
        test_string: String containing the sentence
        blanks: Blank values numbered 1,2,3 etc..
        parts_of_speech: Answewrs corresponding to blank values
        correct_Ans_counter: Counter to number of correct  answers per quiz
    Returns:
        None
    Raises:
        Correct & End of Quiz message
    """
    for f,b in itertools.izip(blanks,parts_of_speech): #loops though all items in list
        i=0 #initialize to 0 to loop though while loop
        incorrect_Ans_counter=len(parts_of_speech) #assign list length of answer to incorrect_Ans_counte
        while i<len(parts_of_speech): #loops though one item in list
            print test_string #print raw string first time and replaced string on subsequent iterations
            user_input2 = raw_input("\nEnter value for " + f) #get user input for blank
            if user_input2.lower()==b: #compare user input with list value if correct
                print "Correct \n" #print correct
                test_string=test_string.replace(f,user_input2.lower())#replace the string with correct user input
                correct_Ans_counter=correct_Ans_counter+1 #count if the number of correct entries matches with the length of list
                if correct_Ans_counter==len(parts_of_speech): #check if correct_Ans_counter has reached the length of list
                    print test_string, "\n \n End of Quiz\n" #Final print with replaced string. End the quiz
                    exit_fn()#Function to exit program
                break #else break while loop and go to for loop to fetch next item
            else:
                i=i+1 #increment i for while loop
                incorrect_Ans_counter=err_incorrect_Ans_counter(i,incorrect_Ans_counter,parts_of_speech) #Call error counter function if user input is incorrect. store the value returned by function

def start_game():
    """Main function to allow user to select difficulty
    Args:
        test string, blank values, Answer values, correct_Ans_counter
    Returns:
        None
    Raises:
        Invalid entry error if user didn't select easy, medium, hard"""
    user_input1 = raw_input("Select your difficulty level: easy, medium, hard \n") #Allow user to select difficulty
    print "You have 3 guesses per blank \n"
    if user_input1.lower()=="easy":
        play_Madlibs("When the going gets _1_, the tough get _2_. Fortune favors the _3_. Tough times never last _1_ people _4_.",["_1_","_2_","_3_","_4_"],
        ["tough", "going", "brave","do"],correct_Ans_counter)
    elif user_input1.lower()=="medium":
        play_Madlibs("Give someone an inch, he/she _1_ take a mile. When the cat's away, the mice _1_ play. Where _2_ is a _1_ , _2_ is _4_ _3_.",["_1_","_2_","_3_","_4_"],["will", "there", "way","a"],correct_Ans_counter)
    elif user_input1.lower()=="hard":
        play_Madlibs("Betty Botter bought some _1_. But she said the _1_ is _2_. If I put it in my batter, it will make my batter _2_.\
        But a bit of _3_ _1_ will make my batter _3_. So twas _3_ Betty Botter bought a _4_ of _3_ _1_",["_1_","_2_","_3_","_4_"],["butter", "bitter", "better","bit"],correct_Ans_counter)
    else:
        print "Invalid input. Quiz will close in 10 seconds" #if user didn't select easy, medium, hard
        exit_fn() #Function to exit program

global incorrect_Ans_counter #variable for incorrect Answer counter
global correct_Ans_counter #variable for correct Answer counter
correct_Ans_counter=0 #initialize correct Answer counter to zero
if __name__ == "__main__":
    start_game() #call main function
