raman_travel_premise = 20
raman_travel_hypothesis = 10

# the hypothesis refers to the number of hours Raman travelled, which is also mentioned in the premise
if raman_travel_hypothesis >= raman_travel_premise:
    # check if the hypothesis value contradicts the estimate of less than 'raman_travel_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Raman travelled
    # any number of hours less than 'raman_travel_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
