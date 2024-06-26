gang_premise = 8
gang_hypothesis = 3

# the hypothesis talks about the number of gang members in a friendship gang, referenced also in the premise
if gang_hypothesis <= gang_premise:
    # check if the hypothesis value contradicts the estimate of 'gang_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members
    # any number of gang members greater than 'gang_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)