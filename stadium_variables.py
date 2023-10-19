from visualizer import *

StadiumTriangleCollectionType = int
STADIUM_TRIANGLE_COLLECTION_SINGLES = StadiumTriangleCollectionType(0)
STADIUM_TRIANGLE_COLLECTION_STRIP = StadiumTriangleCollectionType(1)

StadiumTriangleType = int
STADIUM_TRIANGLE_TYPE_GRASS             = StadiumTriangleType(0x01)
STADIUM_TRIANGLE_TYPE_WALL              = StadiumTriangleType(0x02)
STADIUM_TRIANGLE_TYPE_OOB               = StadiumTriangleType(0x03)
STADIUM_TRIANGLE_TYPE_FOUL_LINE_MARKERS = StadiumTriangleType(0x04)
STADIUM_TRIANGLE_TYPE_BACK              = StadiumTriangleType(0x05)
STADIUM_TRIANGLE_TYPE_DIRT              = StadiumTriangleType(0x06)
STADIUM_TRIANGLE_TYPE_PIT_WALL          = StadiumTriangleType(0x07)
STADIUM_TRIANGLE_TYPE_PIT               = StadiumTriangleType(0x08)
STADIUM_TRIANGLE_TYPE_ROUGH_TERRAIN     = StadiumTriangleType(0x09)
STADIUM_TRIANGLE_TYPE_WATER             = StadiumTriangleType(0x0A)
STADIUM_TRIANGLE_TYPE_CHOMP_HAZARD      = StadiumTriangleType(0x0B)
STADIUM_TRIANGLE_TYPE_FOUL              = StadiumTriangleType(0x80)

def tri_type_to_color(t:StadiumTriangleType):
    b = (255, 0, 255) # magenta
    if   t & 0x0f == STADIUM_TRIANGLE_TYPE_GRASS:               b = (  74, 103,  65 ) # forest green
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_WALL:                b = ( 128, 128, 128 ) # gray
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_OOB:                 b = ( 255, 255,   0 ) # yellow
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_DIRT:                b = ( 165,  92,  42 ) # brown
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_BACK:                b = ( 255, 128, 128 ) # pink
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_PIT_WALL:            b = ( 106,  50, 159 ) # purple
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_PIT:                 b = ( 255,   0,   0 ) # red
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_ROUGH_TERRAIN:       b = (  22,  83, 126 ) # dark blue 
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_WATER:               b = (  69, 212, 255 ) # sky blue 
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_CHOMP_HAZARD:        b = ( 255, 208,  63)  # gold
    elif t & 0x0f == STADIUM_TRIANGLE_TYPE_FOUL_LINE_MARKERS:   b = (   0,   0, 255 ) # blue
    else:
        pass # debug unknown colors

    if t & 0xf0 == 0: pass 
    elif t & 0xf0 == STADIUM_TRIANGLE_TYPE_FOUL: b = (b[0]//2, b[1]//2, b[2]//2)
    else:
        pass
    
    return b

def contrast_color(b:tuple[int, int, int]):
    return ( 
        255-(b[0]//2),
        255-(b[1]//2),
        255-(b[2]//2))

class MssbStadiumVertex:
    def __init__(self) -> None:        
        self.point = Vector3()
        self.stadium_type = StadiumTriangleType(0)

class MssbStadiumVertexList:
    def __init__(self) -> None:
        self.points:list[MssbStadiumVertex] = []
        self.collection_type = StadiumTriangleCollectionType(0)

class MssbStadiumBoundingBox:
    def __init__(self) -> None:        
        self.corner1 = Vector3()
        self.corner2 = Vector3()

        self.triangle_collection:list[MssbStadiumVertexList] = []

class MssbStadium:
    def __init__(self) -> None:
        self.vertex_collection:list[MssbStadiumBoundingBox] = []

def vec3_to_dict(v:Vector3):
    return {
        "X":v.x, 
        "Y":v.y, 
        "Z":v.z
    }

def dict_to_vec3(d:dict):
    return Vector3(d["X"], d["Y"], d["Z"])

def write_stadium(stadium: MssbStadium):
    output = {}
    output["Triangle Collections"] = []

    bBox_collection = stadium.vertex_collection

    for box in bBox_collection:

        this_entry = {
            "BoxCorner1" : vec3_to_dict(box.corner1),
            "BoxCorner2" : vec3_to_dict(box.corner2),
            "Triangles" : []
        }
        
        for collection in box.triangle_collection:
            collection:MssbStadiumVertexList
            
            this_entry["Triangles"].append({
                "CollectionType" : collection.collection_type,
                "Points" : [ 
                    {
                        "CollisionType" : p.stadium_type,
                        "Point" : vec3_to_dict(p.point)
                    } for p in collection.points 
                ]
            })
        output["Triangle Collections"].append(this_entry)
    return output


def read_stadium(d:dict) -> MssbStadium:
    stadium = MssbStadium()

    for d_box in d["Triangle Collections"]:

        this_box = MssbStadiumBoundingBox()
        this_box.corner1 = dict_to_vec3(d_box["BoxCorner1"])
        this_box.corner2 = dict_to_vec3(d_box["BoxCorner2"])

        for d_collection in d_box["Triangles"]:
            collection = MssbStadiumVertexList()
            collection.collection_type = d_collection["CollectionType"]

            for d_point in d_collection["Points"]:
                v = MssbStadiumVertex()
                v.stadium_type = d_point["CollisionType"]
                v.point = dict_to_vec3(d_point["Point"])

                collection.points.append(v)

            this_box.triangle_collection.append(collection)

        stadium.vertex_collection.append(this_box)

    return stadium 
