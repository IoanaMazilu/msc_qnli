gang_premise = 5
gang_hypothesis = 5

# the hypothesis refers to the number of gangs in the premise
if gang_hypothesis <= gang_premise:
    # check if the hypothesis value contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs
    # any number of gangs greater than 'gang_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
