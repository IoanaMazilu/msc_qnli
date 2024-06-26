flights_departed_on_time_premise = 3
flights_departed_on_time_hypothesis = 3
percentage_rate_premise = 40
percentage_rate_hypothesis = 50

# the hypothesis refers to the number of flights and the on-time departure rate mentioned in the premise
if flights_departed_on_time_premise <= flights_departed_on_time_hypothesis:
    # check if the estimate of 'flights_departed_on_time_hypothesis' contradicts the number of flights from the premise
    label = "contradiction"
elif percentage_rate_hypothesis!= percentage_rate_premise:
    # check if the on-time departure rate in the hypothesis contradicts the on-time departure rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
