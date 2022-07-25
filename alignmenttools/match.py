import math

class Match:
    """The generic match object that contains the overlapping parameters between an image an geometrymatch"""

    matchError = math.inf
    matchAmount = 0         #the number of good matches

    def __init__(self) -> None:
        pass

    def find_matches(self):
        """Finds the matches between 2 objects"""

    def get_transformation(self):
        """Returns the estimated transformation between the 2 objects"""

class Match2d (Match):

    def __init__(self) -> None:
        #create a new 2d match instance
        pass


class Match3d (Match):
    
    def __init__(self) -> None:
        #create a new 3d match instance
        pass


