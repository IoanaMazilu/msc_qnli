# Premise: 10% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Hypothesis: less than 70% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Golden Label: entailment

death_rate_premise = 10
death_rate_hypothesis = 70
left_rate_premise = 20
left_rate_hypothesis = 20

# the hypothesis refers to the death and left rates mentioned in the premise
if death_rate_hypothesis < death_rate_premise:
    # check if the estimate of 'death_rate_hypothesis' contradicts the death rate in the premise
    label = "contradiction"
elif left_rate_hypothesis != left_rate_premise:
    # check if the left rate in the hypothesis contradicts the left rate reported in the premise
    label = "contradiction"
elif death_rate_hypothesis > death_rate_premise:
    # the hypothesis gives a larger estimate for the death rate
    # any percentage larger than 'death_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

