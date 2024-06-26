premise = 2
hypothesis = 5

# the hypothesis refers to the number of gang members in Mala's friendship gang
if hypothesis <= premise:
    # check if the hypothesis value contradicts the estimate of more than 'premise' gang members
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members
    # any number of gang members greater than 'premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
