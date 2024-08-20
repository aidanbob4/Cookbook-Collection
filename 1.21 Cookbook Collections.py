import random

class Recipes:
    def __init__(self, name, score, made, page, wish):
        self.name = name
        self.score = score
        self.page = page
        if int(made) == 1:
            self.made = True
        else:
            self.made = False

        if int(wish) == 1:
            self.wish = True
        else:
            self.wish = False

    def setName(self, name):
        self.name = name

    def setMade(self, made):
        self.made = made

    def setScore(self, score):
        self.score = score
        
    def setPage(self, page):
        self.page = page

    def flag(self):
        self.wish = True

class Categories:
    def __init__(self, name, recipes):
        self.name = name
        self.recipes = recipes

    def setRecipes(self, recipes):
        self.recipes = recipes

    def setName(self, name):
        self.name = name


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
        print("[3] Flagged: " + str(rec.wish))
        if int(rec.score) != -1:
            print("[4] Score: " + str(rec.score))
        print("[100] Go Back")

        decision = testInputs(4)
        if decision == 200:
            print("Thats not supposed to happen...")
        elif decision == 100:
            break
        elif decision == 0:
            print("What do you want to change the name too?")
            newName = input()
            rec.setName(newName)
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
            rec.wish = not rec.wish
        elif decision == 4:
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
            if r.wish:
                print("*", end="")
            print("[" + str(count) + "] " + r.name, end="")
            if r.made:
                print(" | " + str(r.score), end="")
            print(" | Pg #" + str(r.page))
            count += 1
        print("[" + str(count) + "] Delete Recipes")
        print("[" + str(count + 1) + "] Flag Recipes")
        print("[100] Add a Recipe")
        print("[200] Go Back")
        decision = testInputs(count + 1)

        if decision == 100:
            recipes = cat.recipes
            recipes.append(addRec())
            cat.setRecipes(recipes)
        elif decision == 200:
            break
        elif decision == count:
            while True:
                print("What recipe do you want to delete?")
                print("[100] I'm done deleting...")
                decision = testInputs(count - 1)

                if decision == 200:
                    print("STOP DOING THIS")
                elif decision == 100:
                    break
                else:
                    print("Are you sure you want to delete " + cat.recipes[decision].name + "?")
                    print("[1] YES")
                    print("[0] NO")
                    while True:
                        try:
                            confirm = int(input())
                            if confirm < 0 or confirm > 1:
                                print("Invalid Try Again")
                            else:
                                break
                        except ValueError:
                            print("Invalid Try Again")

                    if confirm == 1:
                        cat.recipes.pop(decision)
        elif decision == count + 1:
            print("Select as many numbers as you want to flag. Seperate them by spaces. (Ex. 10 20 30)")
            while True:
                while True:
                    try:
                        newFlags = list(map(int, input().strip().split()))
                        break
                    except ValueError:
                        print("Not all of them are numbers...")
                try:
                    for f in newFlags:
                        cat.recipes[f].flag()
                    break
                except IndexError:
                    print("One of these numbers isn't a recipe!")
                    continue 
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
    rand = random.randint(0, len(orgList) - 1)
    print(orgList[rand].name)
    print("Page #" + str(orgList[rand].page))
    

def openCat(cat, book):
    while True:
        print()
        print(cat.name)
        print("What do you want to do?")
        print("[0] View Recipes")
        print("[1] Choose Random Recipe")
        print("[2] Edit Name")
        print("[3] Delete Category")
        print("[200] Go Back")
        decision = testInputs(3)

        if decision == 100:
            print("Hey this isn't supposed to happen...")
        elif decision == 200:
            break
        elif decision == 0:
            showRecs(cat)
        elif decision == 1:
            randRec(cat)
        elif decision == 2:
            print("What do you want to change the name too?")
            newName = input()
            print("Categorie's new name is " + newName)

            cat.setName(newName)
        elif decision == 3:
            while True:   
                print("Are you sure you want to delete the category: " + cat.name)
                print("[1] YES")
                print("[0] NO")
                try:
                    decision = int(input())
                    if decision != 0 and decision != 1:
                        print("Not an option.")
                    else:
                        break
                except ValueError:
                    print("Invalid input")
            if decision == 1:
                book.categories.remove(cat)
                break

def showAllRecs(book):
    while True:
        count = 0
        print()
        print("Recipes in " + book.name)
        for c in book.categories:
            print()
            print(c.name)
            for r in c.recipes:
                print("[" + str(count) + "] " + r.name + " | Page #" + str(r.page))
                count += 1

        print("[9999] Go Back")
        print("Select a recipe to edit or go back")

        while True:
            try:
                decision = int(input())
                if (decision < 0 or decision > count - 1) and decision != 9999:
                    print("Invalid Input")
                else:
                    break
            except ValueError:
                print("Invalid Input")

        if decision == 9999:
            break
        else:
            editRec(r)

def randomAllRecs(book):
    print()
    print("Include made recipes?")
    print("[1] YES")
    print("[0] NO")

    while True:
        try:
            decision = int(input())
            if decision != 0 and decision != 1:
                print("Invalid Input")
            else:
                break
        except ValueError:
            print("Invalid Input")

    recs = []
    
    if decision == 1:
        for c in book.categories:
            for r in c.recipes:
                recs.append(r)
    else:
        for c in book.categories:
            for r in c.recipes:
                if not r.made:
                    recs.append(r)

    recipe = recs[random.randint(0,len(recs) -1)]

    print(recipe.name)
    print("Page #" + str(recipe.page))

def randFlag(flagged):
    print("Include made recipes?")
    print("[1] YES")
    print("[0] NO")
    search = []
    while True:
        try:
            decision = int(input())
            if decision != 1 and decision != 0:
                print("Invalid input")
            else:
                break
        except ValueError:
            print("Invalid input")
    if decision == 0:
        for f in flagged:
            if not f.made:
                search.append(f)
    else:
        search = flagged
    print()
    print("Randomized Flagged Recipe:")
    recipe = search[random.randint(0, len(search) - 1)]
    print(recipe.name)
    print("Page #" + str(recipe.page))
    
        
    
def showFlagged(book):
    while True:
        flagged = []
        print()
        #Identify how much of the book you have cooked!
        recs = 0
        completed = 0
        for c in book.categories:
            for r in c.recipes:
                if r.wish:
                    recs += 1
                    if r.made:
                        completed += 1
        print("(" + str(completed) + "/" + str(recs) + ") " + str(int(completed / recs * 100)) + "%")

        count = 0
        for c in book.categories:
            print()
            print(c.name)
            for r in c.recipes:
                if r.wish:
                    flagged.append(r)
                    print("[" + str(count) + "] " + r.name + " | Page #" + str(r.page))
                    count += 1
                    
        print("[1000] Select Random Recipe")
        print("[9999] Go Back")
        print("Select a recipe to edit or go back")

        while True:
            try:
                decision = int(input())
                if (decision < 0 or decision > count - 1) and decision != 9999 and decision != 1000:
                    print("Invalid Input")
                else:
                    break
            except ValueError:
                print("Invalid Input")

        if decision == 9999:
            break
        elif decision == 1000:
            randFlag(flagged)
            break
        else:
            editRec(flagged[decision])

def openBook(book):
    while True:
        print()
        print()
        print(book.name)

        #Identify how much of the book you have cooked!
        recs = 0
        completed = 0
        for c in book.categories:
            for r in c.recipes:
                recs += 1
                if r.made:
                    completed += 1
        print("(" + str(completed) + "/" + str(recs) + ") " + str(int(completed / recs * 100)) + "%")
        
        print("Choose a category")


        #Select which categorie to access
        for i in range(len(book.categories)):
            print("[" + str(i) + "] " + book.categories[i].name)
            count = i
        print("[" + str(count + 1) + "] View All Recipes")
        print("[" + str(count + 2) + "] Randomly Select a Recipe")
        print("[" + str(count + 3) + "] View Flagged")
        print("[100] Add a New Category")
        print("[200] Go Back") 
        decision = testInputs(count + 3)

        if decision == 100:
            cats = book.categories
            cats.append(addCat())
            book.setCategories(cats)
        elif decision == 200:
            break
        elif decision == count + 1:
            showAllRecs(book)
        elif decision == count + 2:
            randomAllRecs(book)
        elif decision == count + 3:
            showFlagged(book)
        else:
            openCat(book.categories[decision], book)



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

    return Recipes(newName, score, res, page, 0)
    
    
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
        print("[1] YES")
        print("[0] NO")
        decision = testInputs(1)

        if decision == 1:
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
    try:
        f = open("Cookbooks.txt", "r")
    except FileNotFoundError:
        f = open("Cookbooks.txt", "w")
        f.write("0")
        f.close()
        f = open("Cookbooks.txt","r")
    #Add all cookbooks into objects and into the list
    for i in range(int(f.readline())):
        book = f.readline().split()
        cookbooks.append(Cookbook(book[0].replace("_", " "),book[1]))
    
    for c in cookbooks:
        cats = []
        cat = c.categories.split("~")
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
                    newRec.append(Recipes(temp[0].replace("_"," "),temp[1],temp[2],temp[3],temp[4]))
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
                if r.wish:
                    wish = 1
                else:
                    wish = 0
                f.write("=" + r.name.replace(" ","_") + "|" + str(r.score) + "|" + str(temp) + "|" + str(r.page) + "|" + str(wish))
            f.write("~")
        
    
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

