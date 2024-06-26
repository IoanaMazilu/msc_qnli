balls_needed_premise = 3
balls_needed_hypothesis = 4

# the hypothesis refers to the number of balls needed, which is also mentioned in the premise
if balls_needed_hypothesis <= balls_needed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'balls_needed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls needed
    # any number of balls greater than 'balls_needed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)