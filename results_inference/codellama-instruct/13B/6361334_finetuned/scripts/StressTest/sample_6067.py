shops_premise = 5
shops_hypothesis = 4

# the hypothesis refers to the number of shops in the town, which is also mentioned in the premise
if shops_hypothesis <= shops_premise:
    # check if the hypothesis value contradicts the estimate of less than'shops_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shops
    # any number of shops greater than'shops_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
