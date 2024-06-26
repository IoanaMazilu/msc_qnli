y_premise = 20
y_hypothesis = 10

# the hypothesis talks about the number of boxes Kramer can pack per minute, which is also mentioned in the premise
if y_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the estimate of less than 'y_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes less than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
