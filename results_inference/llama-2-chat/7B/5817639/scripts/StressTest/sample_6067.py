town_shops_premise = 5
town_shops_hypothesis = 4

# the hypothesis talks about the number of shops in a town, referenced also in the premise
if town_shops_hypothesis <= town_shops_premise:
    # check if the hypothesis value contradicts the estimate of less than 'town_shops_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shops
    # any number of shops greater than 'town_shops_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
