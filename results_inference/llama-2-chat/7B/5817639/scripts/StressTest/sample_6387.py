balls_given_premise = 100
balls_given_hypothesis = 300

# the hypothesis refers to the number of balls given by John, which is less than the premise
if balls_given_hypothesis <= balls_given_premise:
    # check if the hypothesis value contradicts the estimate of 'balls_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls given,
    # any number of balls given that is less than 'balls_given_premise' is consistent with the premise,
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
