death_rate_premise = 5
death_rate_hypothesis = 4
fearful_departure_rate = 15

# the hypothesis refers to the death rate and the rate of people leaving the village due to fear mentioned in the premise
if death_rate_premise <= death_rate_hypothesis:
    # check if the estimate of 'death_rate_hypothesis' contradicts the death rate in the premise
    label = "contradiction"
elif fearful_departure_rate!= 15:
    # check if the rate of people leaving the village due to fear in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
