cara_leaves_city_a_premise = 90
dan_leaves_city_a_hypothesis = 80

# the hypothesis refers to the time difference between Dan and Cara's departure from City A
if dan_leaves_city_a_hypothesis <= cara_leaves_city_a_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than or equal to 'cara_leaves_city_a_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
