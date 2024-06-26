store_visits_premise = 3
store_visits_hypothesis = 5

# the hypothesis refers to the number of times Daniel went to the store last month, as stated in the premise
if store_visits_hypothesis <= store_visits_premise:
    # check if the hypothesis value contradicts the estimate of more than 'store_visits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of times Daniel went to the store
    # any number of store visits greater than 'store_visits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
