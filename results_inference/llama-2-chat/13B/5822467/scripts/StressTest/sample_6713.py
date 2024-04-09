mike_balls_premise = 17
mike_balls_hypothesis = 77

# the hypothesis refers to the number of balls given by Mike
if mike_balls_hypothesis <= mike_balls_premise:
    # check if the hypothesis value contradicts the estimate of'mike_balls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls greater than'mike_balls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
