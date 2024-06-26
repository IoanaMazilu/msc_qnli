rectangle_premise = 52
rectangle_hypothesis = 12

# the hypothesis talks about the width of Jordan's rectangle, referenced also in the premise
if rectangle_hypothesis <= rectangle_premise:
    # check if the hypothesis value contradicts the estimate of less than'rectangle_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the width of Jordan's rectangle
    # any width greater than'rectangle_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
