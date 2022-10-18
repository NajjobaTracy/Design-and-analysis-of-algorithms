

def searching(list, values):# taking the search list and the value as parameter
    for i in list:
        for j in i:#i being the nested list
            if values == j:
                return i
    return "N"
def main():
    #after research and organising the data is organised
    list = [["A96447","MUGANGA Charles","J22B23/032"],["A94169","KATUKUNDA Rochelle","S21B23/016"],["A94161","NKATA Joshua Luyombya","S21B23/008"],["A95681","NAJJOBA Tracy ","S21B23/034"],["A94169","KATUKUNDA Rochelle","S21B23/016"],["A94160","MUKISA Isaiah","S21B23/007"],["Afghanistan", "93"], 
    ["Fiji", "679"], ["Bahamas", "1-242"],["Tanzania", "255"], ["Saint Vincent and the Grenadines", "1784"],["Ukraine", "380"]]
    countryCode = "7"# search for a country code
    newList = searching(list,countryCode)
    print("I am searching for",countryCode,"and is found",newList[0], "is the country")

    accessNumber="A94160"# search for acess number student
    newList = searching(list,accessNumber)
    print("I am sarching for",accessNumber, "and is found",newList[1], "is the name",newList[2], "is the registration number.")

    countryCode = "380"# search for a country
    newList = searching(list,countryCode)
    print("I am searching for",countryCode,"and is found",newList[0], "is the country")

    Name = "Doe"# search for a student name
    if Name in searching(list,Name):
        print("I am sarching for",Name, "and is found",newList[1], "is the name",newList[2], "is the registration number.")
    else:
        print(Name, "Not in list")
main()
