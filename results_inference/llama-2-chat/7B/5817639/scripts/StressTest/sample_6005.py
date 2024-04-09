balls_premise = 10
balls_hypothesis = 3

# the hypothesis talks about the number of balls needed, referenced also in the premise
if balls_hypothesis <= balls_premise:
    # check if the hypothesis value contradicts the estimate of 'balls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls greater than 'balls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
