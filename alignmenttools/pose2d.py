"""A collection of 2D matching methods
"""

# Import modules
from alignmenttools.match import Match2d
import geomapi
from geomapi.node import Node
from geomapi.sessionnode import SessionNode
from typing import List


def get_transformation(testSession : SessionNode, refSessions : list[SessionNode]):
    pass


# Different Matching methods for 2D objects (images)
def match_incremental(testImage: Node , refImages: List[Node]):
    pass

def match_crossref(testImage: Node , refImages: List[Node]):
    pass

def match_raycast(testImage: Node , refImages: List[Node]):
    pass