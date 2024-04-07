# Premise: 10% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: less than 10% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: contradiction

death_rate_premise = 10
death_rate_hypothesis = 10
flee_rate_premise = 15
flee_rate_hypothesis = 15

# the hypothesis refers to the death rate and flee rate in the premise
if death_rate_hypothesis >= death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate in the premise
    label = "contradiction"
elif flee_rate_hypothesis != flee_rate_premise:
    # check if the flee rate in the hypothesis contradicts the flee rate in the premise
    label = "contradiction"
else:
    # if the death and flee rates values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

