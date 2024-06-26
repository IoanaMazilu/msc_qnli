mala_gang_premise = 2
mala_gang_hypothesis = 5

# the hypothesis talks about the number of gangs Mala has, referenced also in the premise
if mala_gang_hypothesis <= mala_gang_premise:
    # check if the hypothesis value contradicts the estimate of more than'mala_gang_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs Mala has
    # any number of gangs greater than'mala_gang_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
