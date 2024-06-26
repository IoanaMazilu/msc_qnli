balls_given_premise = 100
balls_given_hypothesis = 300

# the hypothesis refers to the number of balls given in the premise
if balls_given_hypothesis <= balls_given_premise:
    # check if the estimate of 'balls_given_hypothesis' contradicts the number of balls given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls greater than 'balls_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
