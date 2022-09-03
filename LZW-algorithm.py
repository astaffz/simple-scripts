import time
import os
ver = "0.1"

## Dictionary
DictIndex = 1
AlgorithmDict = {}
def addtoDict(subject):
    global DictIndex
    AlgorithmDict[subject] = DictIndex
    DictIndex += 1

print("\\ \t SEA-LZW v" + ver)
print("\\ Simple Encoding Application using the Lempel-Ziv-Welch Algorithm")
print("\nPlease enter the sequence of symbols you wish to encode below.")
while(True):
    inp = input("\t>>> ")

    ## A for-loop for the initial dictionary, adds a value to every character in the sequence of symbols
    for i in range(len(inp)):
        if(inp[i] == " "):
            continue
        elif(inp[i] not in AlgorithmDict):
            addtoDict(inp[i])


    ## 'current_char' is initially the character at the input's current index, however , 
    ## if the 'current_char' is already in the algorithm's dictionary, 
    # 'current_char' adds the following characters until it doesn't find a match and adds the new combination of string into the dictionary
    output = ""
    current_char = ""
    for i in range(len(inp)):
        if(i == len(inp)-1):
            testing_chars = current_char + inp[i]
            output += str(AlgorithmDict[testing_chars])
            break
        else:
            testing_chars = current_char + inp[i]  + inp[i+1]

        if(testing_chars not in AlgorithmDict):
            output += str(AlgorithmDict[current_char + inp[i]])
            addtoDict(testing_chars)
            current_char = ""
            
        else:
            current_char = current_char + inp[i]

    print(output)
    inp = input("Do you want to encode another sequence? (Y/N):").upper()
    if(inp == "Y" or inp == "YES"):
        AlgorithmDict = {}
        DictIndex = 1
    else:
        break
print("Thank you for using the SEA-LZW program!")
time.sleep(2)
exit()


                