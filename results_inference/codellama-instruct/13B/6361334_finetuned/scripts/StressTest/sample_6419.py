gang_premise = 3
gang_hypothesis = 7

# the hypothesis refers to the number of gang members in a friendship gang, mentioned in the premise
if gang_hypothesis <= gang_premise:
    # check if the estimate of 'gang_hypothesis' contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members
    # any number of gang members greater than 'gang_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
