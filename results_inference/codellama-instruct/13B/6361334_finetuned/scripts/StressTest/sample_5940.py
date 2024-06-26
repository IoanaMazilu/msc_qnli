gang_mala_premise = 5
gang_mala_hypothesis = 2

# the hypothesis refers to the number of gangs in Mala's friendship gang
if gang_mala_hypothesis <= gang_mala_premise:
    # check if the estimate of 'gang_mala_hypothesis' contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs in Mala's friendship gang
    # any number of gangs greater than 'gang_mala_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
