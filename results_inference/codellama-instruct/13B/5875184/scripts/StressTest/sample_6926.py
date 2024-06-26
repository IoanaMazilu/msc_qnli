premise_gang_count = 8
hypothesis_gang_count = 7

# the hypothesis refers to the number of gang members in a friendship gang
if hypothesis_gang_count >= premise_gang_count:
    # check if the hypothesis value contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of gang members
    # any number of gang members less than 'premise_gang_count' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
