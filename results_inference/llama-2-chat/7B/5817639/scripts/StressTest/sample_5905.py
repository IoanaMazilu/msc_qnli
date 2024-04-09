less_than_7_8_premise = 7
less_than_7_8_hypothesis = 1

# the hypothesis talks about the amount of cookies eaten by Michael
if less_than_7_8_hypothesis <= less_than_7_8_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_7_8_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the amount of cookies eaten by Michael
    # any amount of cookies eaten by Michael consistent with the premise is neutral
    label = "neutral"

print(label)
