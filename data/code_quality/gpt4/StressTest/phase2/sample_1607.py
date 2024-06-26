death_rate_premise = 5
death_rate_hypothesis = 3
fearful_departure_rate = 15

# the hypothesis refers to the rates of death and departure due to fear in a Sri Lankan village mentioned in the premise
if death_rate_hypothesis > death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate reported in the premise
    label = "contradiction"
elif death_rate_hypothesis < death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate reported in the premise
    label = "contradiction"
else:
    # if the rates in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
