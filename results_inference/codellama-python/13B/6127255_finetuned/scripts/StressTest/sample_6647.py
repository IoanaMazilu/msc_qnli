north_america_passengers_premise = 1/12
north_america_passengers_hypothesis = 1/12
europe_passengers = 1/4
africa_passengers = 2/9
asia_passengers = 1/6
other_passengers = 50

# the hypothesis refers to the same distribution of passengers on a ship as in the premise
if north_america_passengers_hypothesis <= north_america_passengers_premise:
    # check if the hypothesis value contradicts the estimate of more than 'north_america_passengers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of north american passengers
    # any number of north american passengers greater than 'north_america_passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
