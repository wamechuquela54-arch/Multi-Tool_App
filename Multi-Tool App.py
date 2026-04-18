#Multi tool app
#calculator
#word counter
#History system
#File saving



print("\n================================")
print("        MULTI-TOOL APP")
print("================================\n")

calc_history = []
word_history = []
equation = ""

#writing calculator history file
def write_calc(calc_history : list,):
    calc_file = open("CalculatorHis.txt" , "w")
    for eq in calc_history:
        calc_file.write(eq + "\n")
    calc_file.close()

#writing word counter history file
def write_word(word_history : list):
    word_file = open("WordHis.txt" , "w")
    for wrd in word_history:
        word_file.write(wrd + "\n")
    word_file.close()

#reading the calculator history file
def read_calc(calc_history : list):
    try:
        calc_reader = open("CalculatorHis.txt" , "r")
        for line in calc_reader:
            calc_history.append(line.strip())
        calc_reader.close()
    except FileNotFoundError:
        print("History not found")

#reading the word counter history file
def read_word(word_history : list):
    try:
        word_reader = open("WordHis.txt" , "r")
        for line2 in word_reader:
            word_history.append(line2.strip())
        word_reader.close()
    except FileNotFoundError:
        print("History not found")

#Defining function calculator
def Calculator(calc_history: list):
    print("\n --- CALCULATOR --- \n")
    while True:
        num1 = float(input("Input first num: "))
        num2 = float(input("Input second num: "))
        op = input("Input the operator (+,-,/,*,^): ")
        if op == "+":
            ans = num1 + num2
        elif op == "-":
            ans = num1 - num2
        elif op == "/":
            if num2 == 0:
                ans = "Undefined big dawg, im not there yet"
            else:
                ans= num1 / num2
        elif op == "*":
            ans = num1 * num2
        elif op == "^":
            ans = num1 ** num2
        else:
            print("Error please try again")
            continue
        equation = str(num1) + " " + op + " " + str(num2) + " = " + str(ans)
        print(equation)
        Continue = input("Do you wish to continue (Yes/No): \n").lower()
        calc_history.append(equation)
        if len(calc_history) > 4:
            calc_history.pop(0)
        if Continue == "no":
            break

#Defining word counter function
def WordCounter(word_history: list):
    print("\n ---WORD COUNTER--- \n")
    text = input("Enter a text in please: \n")
    read= text.replace("?", "")
    read= read.replace(".", "")
    read= read.replace(":", "")
    read= read.replace("!", "")
    read= read.replace(";", "")
    read= read.replace("'", "")
    read= read.replace('"', "")
    read = read.lower()
    words = read.split()
    wrdcount = {}
    for word in words:
        if word in wrdcount:
            wrdcount[word] += 1
        else:
            wrdcount[word] = 1
    data = ""
    for word, counts in wrdcount.items():
        print(word, counts)
        data = data + str(word) + " : " + str(counts) +"\n"
    print("\nTotal words: ", len(words))
    data = data + "\nTotal: " + str(len(words))
    word_history.append(data)
    if len(word_history) > 1:
        word_history.pop(0)

#Loading the history
print("\n LOADING HISTORY... \n")

read_calc(calc_history)
read_word(word_history)


#Main menu
print("\nWELCOME!\n")
while True:
    try:
        choice = int(input("""Choose your next activity:
                    [1]Calculator
                    [2]Word Counter
                    [3]History
                    [4]ToDo lists
                    [5]Exit   
                        :    """))
        if choice == 1:
            Calculator(calc_history)
        elif choice == 2:
            WordCounter(word_history)
        elif choice == 3:
            choice2 = int(input("""Which one:
                                [1]Calculator history 
                                [2]Word counter history
                                  =   """))
            if choice2 == 1:
                if calc_history:
                    print("\n---CALCULATOR HISTORY---")
                    for results in calc_history[-3:]:
                        print(results)
                else:
                    print("No history available gng")
            elif choice2 == 2:
                if word_history:
                    print("\n---WORD COUNTER HISTORY---")
                    for wordings in word_history[-2:]:
                        print(wordings)
                else:
                    print("No history available gng")
        elif choice == 4:
            import ToDo
            ToDo.TaskMenu()
        else:
            end = input("Are you sure?(Yes/No): \n")
            if end.lower() == "yes":
                write_word(word_history)
                write_calc(calc_history)
                print("\n SAVING HISTORY...")
                print("HISTORY SAVED⭐\n")
                print("Goodbye😭")
                break
    except:
        print("INVALID INPUT")
        continue        
    


