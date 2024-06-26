gang_premise = 3
gang_hypothesis = 7

# the hypothesis talks about the number of gangs Angel has, referenced also in the premise
if gang_hypothesis <= gang_premise:
    # check if the hypothesis value contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs
    # any number of gangs greater than 'gang_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
