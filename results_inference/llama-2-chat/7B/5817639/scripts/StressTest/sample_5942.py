gang_size_premise = 5
gang_size_hypothesis = 7

# the hypothesis talks about the number of gang members in a friendship gang, referenced also in the premise
if gang_size_hypothesis <= gang_size_premise:
    # check if the hypothesis value contradicts the estimate of 'gang_size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members
    # any number of gang members greater than 'gang_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
