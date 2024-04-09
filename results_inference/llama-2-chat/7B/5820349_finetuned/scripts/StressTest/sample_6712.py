balls_given_premise = 77
balls_given_hypothesis = 17

# the hypothesis talks about the number of balls given, referenced also in the premise
if balls_given_hypothesis >= balls_given_premise:
    # check if the hypothesis value contradicts the estimate of less than 'balls_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls
    # any number of balls less than 'balls_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
