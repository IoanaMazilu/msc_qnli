# the hypothesis refers to the year 1979 and the number of passengers using Kennedy Airport
if hypothesis_year!= premise_year:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif hypothesis_passengers_per_airport <= premise_passengers_per_airport:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
