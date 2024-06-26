shops_premise = 4
shops_hypothesis = 5

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis <= shops_premise:
    # check if the hypothesis value contradicts the estimate of'shops_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shops
    # any number of shops less than'shops_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
