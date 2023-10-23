from data.constants import HBP_ARRAY, CHARACTER_INDICES, BATTER_HITBOXES, BATTING_REACHES, STATS


def get_hitbox(char_id) -> tuple:
    return HBP_ARRAY[CHARACTER_INDICES[char_id][2]]


def get_box_movement(char_id):
    return BATTER_HITBOXES[char_id]


def get_bat_hitbox(char_id, pos_x, handedness):
    trimmed = 0 if BATTER_HITBOXES[char_id]["TrimmedBat"] == 0.0 else 1
    hb = BATTING_REACHES[trimmed]
    near = pos_x + hb[0]
    far = pos_x + hb[1]

    if handedness == 1:
        near *= -1.0
        far *= -1.0

    return (near, far)


def get_name(char_id) -> str:
    return STATS[char_id]["Name"]
