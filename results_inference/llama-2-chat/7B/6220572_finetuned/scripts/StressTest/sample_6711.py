balls_given_premise = 17
balls_given_hypothesis = 77

# the hypothesis talks about the number of balls given, referenced also in the premise
if balls_given_hypothesis <= balls_given_premise:
    # check if the hypothesis value contradicts the number of balls given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls given
    # any number of balls greater than 'balls_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
