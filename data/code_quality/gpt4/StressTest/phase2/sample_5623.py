dancers_premise = 1
dancers_hypothesis = 4

# the hypothesis talks about the number of dancers, referenced also in the premise
if dancers_hypothesis <= dancers_premise:
    # check if the hypothesis value contradicts the estimate of more than 'dancers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of dancers
    # any number of dancers greater than 'dancers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
