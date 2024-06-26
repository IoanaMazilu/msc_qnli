gang_mala_premise = 5
gang_mala_hypothesis = 5

# the hypothesis refers to the number of gang members in Mala's friendship gang
if gang_mala_hypothesis <= gang_mala_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gang_mala_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members in Mala's friendship gang
    # any number of gang members greater than 'gang_mala_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
