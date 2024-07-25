import random

class Recipes:
    def __init__(self, name, score, made, page):
        self.name = name
        self.score = score
        self.page = page
        if int(made) == 1:
            self.made = True
        else:
            self.made = False

    def setName(self, name):
        self.name = name

    def setMade(self, made):
        self.made = made

    def setScore(self, score):
        self.score = score
        
    def setPage(self, page):
        self.page = page

class Categories:
    def __init__(self, name, recipes):
        self.name = name
        self.recipes = recipes

    def setRecipes(self, recipes):
        self.recipes = recipes


class Cookbook:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def setCategories(self, categories):
        self.categories = categories
    

#Variables
cookbooks = []

def testInputs(count):
    while True:
        try:
            decision = int(input())
            if (decision >= 0 and decision <= count) or decision == 100 or decision == 200:
                break
            else:
                print("Invalid! Please try again!")
        except ValueError:
            print("Invalid! Please try again!")
    return decision

def editRec(rec):
    while True:
        print()
        print(rec.name)
        print("What do you want to change?")
        print("[0] Name: " + str(rec.name))
        print("[1] Made: " + str(rec.made))
        print("[2] Page: " + str(rec.page))
        if int(rec.score) != -1:
            print("[3] Score: " + str(rec.score))
        print("[100] Go Back")

        decision = testInputs(3)
        if decision == 200:
            print("Thats not supposed to happen...")
        elif decision == 100:
            break
        elif decision == 0:
            print("What do you want to change the name too?")
            newName = input()
            rec.setName = newName
        elif decision == 1:
            make = not rec.made
            rec.setMade(make)
            if make:
                print("What score do you give it out of 10? (It can go above 10... and include decimals)")
                while True:
                    try:
                        decision = float(input())
                        if decision < 0:
                            print("Not a positive number!")
                        else:
                            break
                    except ValueError:
                        print("Not a float or an integer...")
                rec.setScore(decision)
            else:
                rec.setScore(-1)
        elif decision == 2:
            print("Whats the page number?")
            while True:
                    try:
                        decision = int(input())
                        if decision < 0:
                            print("Not a positive number!")
                        else:
                            break
                    except ValueError:
                        print("Not an integer...")
            rec.setPage(decision)
        elif decision == 3:
            if score == -1:
                print("You're not supposed to be here yet... get to cooking.")
            else:
                print("What do you want to change the score to?")
                while True:
                    try:
                        decision = float(input())
                        if float < 0:
                            print("Not a positive number!")
                        else:
                            break
                    except ValueError:
                        print("Not a float or an integer...")
                rec.setScore(decision)
                
                        

    
def showRecs(cat):
    while True:
        print()
        print(cat.name + " Recipes")
        count = 0
        for r in cat.recipes:
            print("[" + str(count) + "] " + r.name, end="")
            if r.made:
                print(" | " + str(r.score), end="")
            print(" | Pg. " + str(r.page))
            count += 1
        print("[100] Add a Recipe")
        print("[200] Go Back")
        decision = testInputs(count - 1)

        if decision == 100:
            recipes = cat.recipes
            recipes.append(addRec())
            cat.setRecipes(recipes)
        elif decision == 200:
            break
        else:
            editRec(cat.recipes[decision])

def randRec(cat):
    print("Do you want to include already made recipes? [Y]es")
    dec = input().lower()
    orgList = []
    if dec != "y":
        for r in cat.recipes:
            if not r.made:
                orgList.append(r)
    else:
        orgList = cat.recipes
    rand = random.randint(0, len(orgList))
    print(orgList[rand].name)
    print("Page #" + str(orgList[rand].page))
    

def openCat(cat):
    while True:
        print()
        print(cat.name)
        print("What do you want to do?")
        print("[0] View Recipes")
        print("[1] Choose Random Recipe")
        print("[200] Go Back")
        decision = testInputs(1)

        if decision == 100:
            print("Hey this isn't supposed to happen...")
        elif decision == 200:
            break
        elif decision == 0:
            showRecs(cat)
        elif decision == 1:
            randRec(cat)
    
def openBook(book):
    while True:
        print()
        print()
        print(book.name)
        print("Choose a category")


        #Select which categorie to access
        for i in range(len(book.categories)):
            print("[" + str(i) + "] " + book.categories[i].name)
            count = i
        print("[100] Add a new category")
        print("[200] Go Back") 
        decision = testInputs(count)

        if decision == 100:
            cats = book.categories
            cats.append(addCat())
            book.setCategories(cats)
        elif decision == 200:
            break
        else:
            openCat(book.categories[decision])



def addRec():
    print()

    #Confirm name of the recipe
    print()
    print("What is the new recipe's name?")
    name = input()

    newName = name

    print("Have you made this recipe before?")
    print("[1] YES")
    print("[0] NO")
    res = testInputs(1)


    print("What page is it on?")
    while True:
        try:
            page = int(input())
            break
        except ValueError:
            print("Not a number!")
            
    if res == 1:
        made = True
    else:
        made = False

    score = -1
    if made:
        print("What would you give it on a scale of 1-10? (You are allowed to go over if you wish...)")
        while True:
            try:
                score = float(input())
                if score < 0:
                    print("Must be a positive number! Try Again!")
                else:
                    break
            except ValueError:
                print("Not a number/decimal! Try again!")

    return Recipes(newName, score, res, page)
    
    
def addCat():
    print()

    recipes = []
    
    #Confirm name of the Category
    while True:
        print()
        print("What is the new category's name?")
        name = input()

        print("Are you sure the name of the category is: " + name)
        print("[1] YES")
        print("[0] NO")
        decision = testInputs(1)

        if decision == 1:
            break

    while True:
        print()
        print("Add a recipe?")
        print("[1] YES")
        print("[0] NO")
        decision = testInputs(1)

        if decision == 1:
            recipes.append(addRec())
        else:
            break

    return Categories(name, recipes)

def addBook():
    f = open("Cookbooks.txt", "a")
    print()

    #Variables
    categories = []

    #Confirm name of the Book
    while True:
        print()
        print("What is the new cookbook's name?")
        name = input()

        print("Are you sure the name of the cookbook is: " + name)
        print("[0] YES")
        print("[1] NO")
        decision = testInputs(1)

        if decision == 0:
            break

    while True:
        print()
        print("Add a category?")
        print("[1] YES")
        print("[0] NO")
        decision = testInputs(1)

        if decision == 1:
            categories.append(addCat())
        else:
            break
        
    cookbooks.append(Cookbook(name, categories)) 
    print("Returning...")
    print("...")

            
def openFile():
    f = open("Cookbooks.txt", "r")
    #Add all cookbooks into objects and into the list
    for i in range(int(f.readline())):
        book = f.readline().split()
        cookbooks.append(Cookbook(book[0].replace("_", " "),book[1]))
    
    for c in cookbooks:
        cats = []
        cat = c.categories.split(":")
        #print(cat)

        #Create objects out of categories
        for i in range(len(cat)):
            if i != len(cat) - 1:
                rec = []
                newRec = []
                newCat = cat[i].split("=")
                #print(newCat)

                #Create a list of recipes for each category
                for _ in range(len(newCat)):
                    if _ != 0:
                        rec.append(newCat[_])

                catObj = Categories(newCat[0].replace("_"," "),rec)
                cats.append(catObj)

                #Create objects out of recipes
                for r in rec:
                    temp = r.split("|")
                    newRec.append(Recipes(temp[0].replace("_"," "),temp[1],temp[2],temp[3]))
                catObj.setRecipes(newRec)
        c.setCategories(cats)
        
def save():
    f = open("Cookbooks.txt", "w")
    f.write(str(len(cookbooks)))
    for c in cookbooks:
        f.write("\n" + c.name.replace(" ","_") + " ")
        for cat in c.categories:
            f.write(cat.name.replace(" ","_"))
            for r in cat.recipes:
                if r.made:
                    temp = 1
                else:
                    temp = 0
                f.write("=" + r.name.replace(" ","_") + "|" + str(r.score) + "|" + str(temp) + "|" + str(r.page))
            f.write(":")
        
    
openFile()
while True:
    print()
    print()
    print()
    #Choices for which cookbook you want to access
    print("Select which cookbook you want to work with!")
    count = 0
    for i in range(len(cookbooks)):
        print("[" + str(i) + "] " + cookbooks[i].name)
        count = i
    print("[100] Add a new cookbook")
    print("[200] Close and Save")
    decision = testInputs(count)

    if decision == 100:
        addBook()
    elif decision == 200:
        save()
        break
    else:
        openBook(cookbooks[decision])

