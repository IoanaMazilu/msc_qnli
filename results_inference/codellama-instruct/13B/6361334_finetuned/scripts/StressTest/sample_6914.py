flights_departed_premise = 3
flights_departed_hypothesis = 3
on_time_departures_premise = 70
on_time_departures_hypothesis = 50

# the hypothesis refers to the number of flights departed on-time and the on-time departure rate
if flights_departed_premise!= flights_departed_hypothesis:
    # check if the number of flights departed in the hypothesis contradicts the number of flights departed in the premise
    label = "contradiction"
elif on_time_departures_hypothesis <= on_time_departures_premise:
    # check if the on-time departure rate in the hypothesis contradicts the on-time departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
