gang_andrew_premise = 8
gang_andrew_hypothesis = 3

# the hypothesis talks about the number of gangs Andrew has, referenced also in the premise
if gang_andrew_hypothesis <= gang_andrew_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gang_andrew_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs Andrew has
    # any number of gangs greater than 'gang_andrew_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
