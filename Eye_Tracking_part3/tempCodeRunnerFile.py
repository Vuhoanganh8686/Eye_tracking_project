 creating pixel counter function 
def pixelCounter(first_piece, second_piece, third_piece):
    # counting black pixel in each part 
    right_part = np.sum(first_piece == 0)
    center_part = np.sum(second_piece == 0)
    left_part = np.sum(third_piece == 0 )
    # creating list of these values
    eye_parts = [right_part, center_part, left_part]

    # getting the index of max values in the list 
    max_index = eye_parts.index(max(eye_parts))
    pos_eye ='' 
    if max_index == 0:
        pos_eye="LEFT"
        color=[utils.BLACK, utils.GREEN]
    elif max_index == 1:
        pos_eye = 'CENTER'
        color = [utils.YELLOW, utils.PINK]
    elif max_index == 2:
        pos_eye = 'RIGHT'
        color = [utils.GRAY, utils.YELLOW]
    else:
        pos_eye = "Closed"
        color = [utils.GRAY, utils.YELLOW]
    return pos_eye, color