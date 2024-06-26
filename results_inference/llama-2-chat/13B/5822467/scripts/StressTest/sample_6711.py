balls_premise = 17
balls_hypothesis = 77

# the hypothesis refers to the number of balls given by Mike
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the estimate of 'balls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls less than 'balls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
