"""A collection of 2D matching methods
"""

# Import modules
import alignmenttools
from alignmenttools.match import Match, Match2d
import geomapi
from geomapi.node import Node
from geomapi.sessionnode import SessionNode
from typing import List

# Calculates a number of estimated positions from different 2D pose estimation methods
def get_transformation(testSession : SessionNode, refSessions : list[SessionNode]):
    pass


# Different Matching methods for 2D objects (images)

# Searches for the best match in the refImages, then searches for its best match in the other refimages
# Creates a match between the 2 linked images and iterrates the third one. using pnp pose
def match_incremental(testImage: Node , refImages: List[Node]):
    # Find the best test-ref image match
    # Find the best ref-ref image match with the chosen ref image
    # Calculate the transformation of the ref-ref-match
    # Get the PnP pose of the test image
    # return a transformation matrix and the matches
    pass

def match_crossref(testImage: Node , refImages: List[Node]):
    # Find the 2 best test-ref image match
    # Calculate the transformation of each of the matches
    # Find the closest point between the 2 direction
    # return a transformation matrix and the matches
    pass

def match_raycast(testImage: Node , refImages: List[Node], geometry: Node):
    pass



def get_best_session_match(image: Node , imageList: List[Node]):
    """Finds the best match in the same session"""

    if(image not in imageList): 
        print("ERROR: Image not in list")
        return None
    newList = imageList.copy()
    newList.remove(image)
    bestRefMatch = get_best_matches(image, newList)
    #Calculate the 3D points in the scene with the know real world locations of the 2 reference images
    
    bestRefMatch.get_essential_matrix() #calculate the essential matrix and inliers
    bestRefMatch.get_reference_scaling_factor() # get the scene scale by using the real world distances
    bestRefMatch.triangulate(True) #calulate the 3d points

    return bestRefMatch

# Check a test image against a list of reference images. Returns a list of the "nr" best matches
def get_best_matches(testImage, refImages, nr: int = 1) -> Match:
    results = [] # a list of all the results
    bestResults = [] # a list of the best results
    nrCheck = 0
    totalCheck = len(refImages)

    for refImage in refImages:
            newMatch = Match2d(refImage, testImage) #create a new match between 2 images
            newMatch.find_matches() # find the best matches 
            results.append(newMatch)

            # check if the newResult is in the top of results
            bestResults.append(newMatch)
            bestResults = sorted(bestResults, key= lambda x: x.matchError) #sort them from low to High
            if(len(bestResults) > nr): #remove the worst match
                bestResults = bestResults[:nr]

            nrCheck +=1
            print(str(nrCheck) + "/" + str(totalCheck) + " checks complete with matchError:" + str(newMatch.matchError))

    for result in bestResults:
        result.get_transormation() # determin the transformation and inliers

    if(nr == 1): return bestResults[0]
    return bestResults