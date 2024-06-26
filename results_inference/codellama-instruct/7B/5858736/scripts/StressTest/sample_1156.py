premise_passengers_total = 37.3
premise_passengers_airport = 1/3
premise_passengers_airport_time = "less than 2979"

hypothesis_passengers_total = 37.3
hypothesis_passengers_airport = 1/3
hypothesis_passengers_airport_time = "1979"

# the hypothesis talks about the number of passengers using Kennedy Airport, referenced also in the premise
if hypothesis_passengers_airport_time!= premise_passengers_airport_time:
    # check if the time period in the hypothesis contradicts the time period reported in the premise
    label = "contradiction"
elif hypothesis_passengers_airport <= premise_passengers_airport:
    # check if the estimate of 'hypothesis_passengers_airport' contradicts the number of passengers using Kennedy Airport in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
