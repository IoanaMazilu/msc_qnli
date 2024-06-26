flights_departed_on_time_premise = 3
flights_departed_on_time_hypothesis = 3
departure_rate_target_premise = 0.8
departure_rate_target_hypothesis = 0.7

# the hypothesis refers to the number of flights that need to depart on-time for the airport's on-time departure rate to be higher than a certain percentage, which is also mentioned in the premise
if flights_departed_on_time_hypothesis <= flights_departed_on_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'flights_departed_on_time_premise'
    label = "contradiction"
elif departure_rate_target_hypothesis < departure_rate_target_premise:
    # check if the target departure rate in the hypothesis is less than the target departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
