import math
import cv2

import alignmenttools.params as params

class Match:
    """The generic match object that contains the overlapping parameters between an image an geometrymatch"""

    matchError = math.inf
    matchAmount = 0         #the number of good matches

    def __init__(self, resource1, recourse2) -> None:
        pass
    
    # The initial matching to evaliaute the quality of the match
    def find_matches(self):
        """Finds the matches between 2 objects"""

    # The full transormation calculation
    def get_transformation(self):
        """Returns the estimated transformation between the 2 objects"""

class Match2d (Match):

    def __init__(self, image1,  image2) -> None:
        #create a new 2d match instance
        self.image1 = image1
        self.image2 = image2

    def find_matches(self):
        """Finds matches between the 2 images"""
        if(self.matches is None):
            # get cv2 ORb features
            self.image1.get_cv2_features(params.MAX_2D_FEATURES)
            self.image2.get_cv2_features(params.MAX_2D_FEATURES)
            # Match features.
            matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = matcher.match(self.image1.descriptors, self.image2.descriptors, None)
            # Sort matches by score
            matches = sorted(matches, key = lambda x:x.distance)
            # only use the best features
            if(len(matches) < params.MAX_2D_MATCHES):
                print("only found", len(matches), "good matches")
                matchError = math.inf
            else:
                matches = matches[:params.MAX_2D_MATCHES]
                # calculate the match score
                # right now, it's just the average distances of the best points
                matchError = 0
                for match in matches:
                    matchError += match.distance
                matchError /= len(matches)
            self.matches = matches
            self.matchError = matchError
            self.matchAmount = len(matches)
        return self.matches


class Match3d (Match):
    
    def __init__(self) -> None:
        #create a new 3d match instance
        pass


