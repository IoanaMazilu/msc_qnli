year_premise = 1979
airline_passengers_premise = 37.3
airline_passengers_hypothesis = 37.3

# the hypothesis refers to the number of airline passengers using Kennedy Airport, also mentioned in the premise
if year_premise!= 1979 or airline_passengers_hypothesis!= airline_passengers_premise:
    # check if the year or number of passengers in the hypothesis contradicts the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the year and the number of passengers
    # any number of passengers consistent with the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
