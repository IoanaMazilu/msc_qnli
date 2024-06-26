gang_premise = 5
gang_hypothesis = 8

# the hypothesis talks about the number of gang Andrew has, referenced also in the premise
if gang_hypothesis <= gang_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gang_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang
    # any number of gang greater than 'gang_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
