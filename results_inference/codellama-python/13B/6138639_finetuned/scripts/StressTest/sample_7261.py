carol_rectangle_premise = 52
carol_rectangle_hypothesis = 12
jordan_rectangle_premise = 9
jordan_rectangle_hypothesis = 9

# the hypothesis talks about the dimensions of Carol's and Jordan's rectangles, referenced also in the premise
if carol_rectangle_hypothesis >= carol_rectangle_premise:
    # check if the hypothesis value contradicts the estimate of less than 'carol_rectangle_premise'
    label = "contradiction"
elif jordan_rectangle_hypothesis!= jordan_rectangle_premise:
    # check if the length of Jordan's rectangle in the hypothesis contradicts the length of Jordan's rectangle reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the dimensions of Carol's rectangle
    # any dimensions of Carol's rectangle less than 'carol_rectangle_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
