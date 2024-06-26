carol_rectangle_length = 52
carol_rectangle_width = 15
jordan_rectangle_length = 9

# the hypothesis talks about the length of Jordan's rectangle, referenced also in the premise
if jordan_rectangle_length <= carol_rectangle_width:
    # check if the hypothesis value contradicts the estimate of 'carol_rectangle_width'
    label = "contradiction"
else:
    # the premise gives only an estimate for the width of Carol's rectangle
    # any number of inches greater than 'carol_rectangle_width' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
