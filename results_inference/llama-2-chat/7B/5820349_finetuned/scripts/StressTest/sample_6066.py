shops_premise = 4
shops_hypothesis = 5

# the hypothesis talks about the number of shops in a town, referenced also in the premise
if shops_hypothesis <= shops_premise:
    # check if the hypothesis value contradicts the estimate of less than'shops_hypothesis'
    label = "contradiction"
elif shops_hypothesis > shops_premise:
    # the premise gives an estimate for the number of shops
    # any number of shops less than'shops_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
