# Premise: 10% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Hypothesis: more than 10% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Golden Label: contradiction

death_rate_premise = 10
death_rate_hypothesis = 10
left_rate = 20

# The hypothesis talks about the death rate and the rate of people who left the village, both of which are also mentioned in the premise
if death_rate_hypothesis > death_rate_premise:
    # Check if the death rate in the hypothesis contradicts the death rate in the premise
    label = "contradiction"
elif death_rate_hypothesis < death_rate_premise:
    # Check if the death rate in the hypothesis contradicts the death rate in the premise
    label = "contradiction"
else:
    # If the death rate and the rate of people who left in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

