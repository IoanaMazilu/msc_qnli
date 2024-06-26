death_rate_premise = 5
death_rate_hypothesis = 4
flee_rate_premise = 20
flee_rate_hypothesis = 20

# the hypothesis talks about the rates of death and fleeing in a village in Sri Lanka, referenced also in the premise
if death_rate_premise != death_rate_hypothesis:
    # check if the death rate in the hypothesis contradicts the death rate provided in the premise
    label = "contradiction"
elif flee_rate_premise != flee_rate_hypothesis:
    # check if the rate of people who left the village in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis rates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
