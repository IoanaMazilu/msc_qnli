balls_given_premise = 100
balls_given_hypothesis = 300

# the hypothesis talks about the number of balls given by John, referenced also in the premise
if balls_given_hypothesis <= balls_given_premise:
    # check if the hypothesis value contradicts the estimate of less than 'balls_given_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number for the number of balls given
    # any number of balls less than 'balls_given_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
