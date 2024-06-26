pies_baked_premise = 310
pies_baked_hypothesis = 810

# the hypothesis refers to the number of pies baked by Anitha, which is also mentioned in the premise
if pies_baked_hypothesis <= pies_baked_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'pies_baked_premise' pies
    label = "contradiction"
else:
    # the premise only gives an estimate for the number of pies
    # any number of pies greater than 'pies_baked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
