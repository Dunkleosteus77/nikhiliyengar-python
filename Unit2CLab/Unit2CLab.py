ToDoList="Go to work", "Go to work", "Go to work", "Go to work"

numList=[1,2,3,4,5,6,7,8,9,10]
#print(numList)
#print(len(numList))
#print(numList[0])
#print(numList[9])

subList=numList[0:5]
print(subList)
print(subList+[6])
number=subList.append(5)
print(subList)

myClasses = ["Stats", "Economics", "Psych", "Finance", "Python"]
print(myClasses)
myClasses.remove("Stats")
print(myClasses)
favClass = myClasses.pop(3)
print(favClass)

