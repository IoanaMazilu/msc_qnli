kennedy_airport_passengers_premise = 37300000
kennedy_airport_passengers_hypothesis = 37300000
year_premise = 1979
year_hypothesis = 7979

# the hypothesis refers to the number of airline passengers using Kennedy Airport in two different years
if kennedy_airport_passengers_hypothesis <= kennedy_airport_passengers_premise:
    # check if the estimate of 'kennedy_airport_passengers_hypothesis' contradicts the number of passengers using Kennedy Airport in the premise
    label = "contradiction"
elif year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
