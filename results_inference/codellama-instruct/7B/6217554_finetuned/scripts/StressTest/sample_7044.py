travel_hours_premise = 10
travel_hours_hypothesis = 20

if travel_hours_hypothesis <= travel_hours_premise:
    # check if the hypothesis value contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'travel_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
