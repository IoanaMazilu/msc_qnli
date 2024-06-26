gang_size_premise = 8
gang_size_hypothesis = 8

# the hypothesis refers to the number of gang members Andrew has, also mentioned in the premise
if gang_size_hypothesis >= gang_size_premise:
    # check if the estimate of 'gang_size_hypothesis' contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members
    # any number of gang members less than 'gang_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
