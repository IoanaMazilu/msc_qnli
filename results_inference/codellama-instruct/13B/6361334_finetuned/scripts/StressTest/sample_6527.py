flights_departed_premise = 3
flights_departed_hypothesis = 3
on_time_departures_premise = 60
on_time_departures_hypothesis = 20

# the hypothesis refers to the number of flights departed on-time and the on-time departure rate
if flights_departed_premise!= flights_departed_hypothesis:
    # check if the number of flights departed in the hypothesis contradicts the number of flights departed in the premise
    label = "contradiction"
elif on_time_departures_hypothesis >= on_time_departures_premise:
    # check if the on-time departure rate in the hypothesis is higher than the on-time departure rate in the premise
    label = "entailment"
else:
    # if the on-time departure rate in the hypothesis is lower than the on-time departure rate in the premise, we cannot infer entailment
    label = "neutral"

print(label)
