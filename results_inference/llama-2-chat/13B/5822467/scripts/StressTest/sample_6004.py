balls_premise = 10
balls_hypothesis = 4

# the hypothesis refers to the number of balls John needs, mentioned in the premise
if balls_premise <= balls_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'balls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls John needs
    # any number of balls greater than 'balls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
