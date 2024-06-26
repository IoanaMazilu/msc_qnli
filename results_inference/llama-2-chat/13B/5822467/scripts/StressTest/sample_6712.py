balls_premise = 77
balls_hypothesis = 17

# the hypothesis refers to the number of balls given by Mike
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the estimate of less than 'balls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls greater than 'balls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)