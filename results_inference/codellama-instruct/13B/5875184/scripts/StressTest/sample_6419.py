premise_gang = 3
hypothesis_gang = 7

# the hypothesis refers to the number of gang members in a friendship gang
if hypothesis_gang <= premise_gang:
    # check if the hypothesis value contradicts the estimate of 'premise_gang'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members
    # any number of gang members greater than 'premise_gang' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
