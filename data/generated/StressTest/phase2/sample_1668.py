# Premise: 5% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: more than 1% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: entailment

death_rate_premise = 5
death_rate_hypothesis = 1
left_rate_premise = 15
left_rate_hypothesis = 15

# the hypothesis refers to the death and leaving rates mentioned in the premise
if death_rate_premise < death_rate_hypothesis:
    # check if the estimate of 'death_rate_hypothesis' contradicts the death rate in the premise
    label = "contradiction"
elif left_rate_hypothesis != left_rate_premise:
    # check if the leaving rate in the hypothesis contradicts the leaving rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

