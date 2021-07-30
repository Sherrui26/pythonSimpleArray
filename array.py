
thisArray = ["Simple", "Array", "Example"]
y = list(thisArray)
y[1] = "Replaced"
thisArray = tuple(y)
print(thisArray)
