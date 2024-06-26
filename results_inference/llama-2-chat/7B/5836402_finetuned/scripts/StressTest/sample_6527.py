flights_departed_premise = 3
flights_departed_hypothesis = 3
rate_premise = 60
rate_hypothesis = 20

# the hypothesis refers to the number of flights that need to depart on-time from Phoenix to reach a higher departure rate than 20%
# the premise refers to the number of flights that need to depart on-time from Phoenix to reach a higher departure rate than 60%
if flights_departed_premise <= flights_departed_hypothesis:
    # check if the estimate of 'flights_departed_hypothesis' contradicts the number of flights needed for the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the departure rate in the hypothesis contradicts the departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
