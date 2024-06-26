death_rate_premise = 10
death_rate_hypothesis = 10
left_rate_premise = 20
left_rate_hypothesis = 20

# the hypothesis refers to the death rate and the departure rate of a village in Sri Lanka mentioned in the premise
if death_rate_hypothesis!= death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate reported in the premise
    label = "contradiction"
elif left_rate_hypothesis!= left_rate_premise:
    # check if the departure rate in the hypothesis contradicts the departure rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
