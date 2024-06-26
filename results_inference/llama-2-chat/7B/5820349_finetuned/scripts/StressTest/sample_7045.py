travel_hours_premise = 20
travel_hours_hypothesis = 10

# the hypothesis refers to the number of hours Raman travelled, also mentioned in the premise
if travel_hours_hypothesis >= travel_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Raman travelled
    # any number of hours less than 'travel_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
