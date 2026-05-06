
class Institution:
    __institutionId = 0
    __institutionName =""
    __noOfStudentsPlaced = 0
    __noOfStudentsCleared = 0
    __location = ""
    __grade = ""
    
    def __init__ (self, institutionId, institutionName, noOfStudentsPlaced, noOfStudentsCleared, location, grade):
        self.__institutionId = institutionId
        self.__institutionName = institutionName
        self.__noOfStudentsPlaced = noOfStudentsPlaced
        self.__noOfStudentsCleared = noOfStudentsCleared
        self.__location = location
        self.__grade = grade
        
        # getter
        def getinstituionId(self):
            return self.__institutionId
        def getinstitutionName(self):
            return self.__institutiionName
        def getnoOfStudentsPlaced(self):
            return self.__noOfStudentsPlaced
        def getnoOfStudentsCleared(self):
            return self.__noOfStudentsCleared
        def getlocation(self):
            return self.__location
        def getgrade(self):
            return self.__grade
        
        # setter
        def setinstitutionId(self, institutionId):
            self.__institutonId = institutionId
        def setinstitutionName(self, institutionName):
            self.__institutionName = institutionName
        def setnoOfStudentsPlaced(self, noOfStudentsPlaced):
            self.__noOfStudentsPlaced = noOfStudentsPlaced
        def setnoOfStudentsCleared(self, noOfStudentsCleared):
            self.__noOfStudentsCleared = noOfStudentsCleared
        def setlocation(self, location):
            self.__location = location
        def setgrade(self, grade):
            self.__grade = grade
            
class Solution:
    @staticmethod
    def FindNumClearanceByLoc(instituion, location):
        total_cleared = 0