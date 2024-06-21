class studentInfo:
    def __init__(self):
        pass

    def setClass(self, classNo):
        self.classNo = str(classNo)
        self.classData = open("data/classes.txt", "a")
        self.classData.write(self.classNo+"\n")
        self.classData.close()
        print("Class added successfully")

    def getClass(self):
        return self.classNo
    
    def addStudent(self, stuIden, studentName):
        # stuIden (Class + Student Number) is a derived variable with total 4 char
        self.stuIden = str(stuIden)
        if stuIden[0].isdigit() == False:
            raise ValueError("The first character should be the form number.")
        if stuIden[1].isalpha() == False:
            raise ValueError("The second character should be the class character.")
        if len(stuIden) != 4:
            raise ValueError("Please enter a valid value with 4 characteers.  E.g. \'1A01\'")
        self.studentName = studentName
        
        # Add the stuIden and studentName to file
        self.studentData = open("data/students.txt", "a")
        self.studentData.write(self.stuIden  + "\t" + self.studentName + "\n")
        self.studentData.close()
        
    def classList(self, classNo):    # TODO: check need private or not
        cList = list()
        self.classNo = classNo

    def recentlyTeaching(self):
        self.teaching = open("data/classes.txt", "r")
        self.strTeaching = str()
        self.strTeaching.join(self.teaching.readlines())
        self.teaching.close()
        return self.strTeaching
    
    def reset(self, filepath):
        # TODO: MUST ADD VERIFICATION TO RESET ALL DATA
        # TMEP CLI Verification
        print(f"Are you sure to reset {filepath}? (Yes / No): ")
        verifyResetStr = input()
        if verifyResetStr == "Yes":
            self.resetClassFile = open(filepath, "r")
            line = 0
            char = 0

            # Find total number of characters in file
            for l in self.resetClassFile:
                wordList = l.split()
                line += 1
                char += len(l)

            self.resetClassFile.close()
            self.resetClassFile = open(filepath, "w")
            self.resetClassFile.seek(char)
            self.resetClassFile.write("\b"*char)
            self.resetClassFile.close()

        

                                   
class assignment(studentInfo):
    def addAssignment(self, assName):
        self.assName = assName

    def setMark(self, stuIden, assName, mark):
        self.data = list()
        self.record = (stuIden, assName, mark)
        
##########
## TODO: Assign student to a class.