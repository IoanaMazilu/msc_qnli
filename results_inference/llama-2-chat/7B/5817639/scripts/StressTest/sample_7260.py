rectangle_premise = 12
rectangle_hypothesis = 9

# the hypothesis talks about the size of Jordan's rectangle, referenced also in the premise
if rectangle_hypothesis <= rectangle_premise:
    # check if the hypothesis value contradicts the estimate of less than'rectangle_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of Jordan's rectangle
    # any size less than'rectangle_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
