shops_town_premise = (4, 5)
shops_town_hypothesis = (4, 5)

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_town_hypothesis[0] >= shops_town_premise[0] or shops_town_hypothesis[1] <= shops_town_premise[1]:
    # check if the hypothesis values contradict the estimate of more than'shops_town_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shops
    # any number of shops greater than'shops_town_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
