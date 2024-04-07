# Premise: 10% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Hypothesis: 30% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Golden Label: contradiction

death_rate_premise = 10
death_rate_hypothesis = 30
migration_rate_premise = 20
migration_rate_hypothesis = 20

# the hypothesis talks about the percentage of people who died and who left the village, both referenced also in the premise
if death_rate_hypothesis != death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate mentioned in the premise
    label = "contradiction"
elif migration_rate_hypothesis != migration_rate_premise:
    # check if the migration rate in the hypothesis contradicts the migration rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

