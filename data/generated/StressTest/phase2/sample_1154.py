# Premise: 8% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: more than 8% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: contradiction

death_rate_premise = 8
death_rate_hypothesis = 8
migration_rate_premise = 15
migration_rate_hypothesis = 15

# the hypothesis refers to the death and migration rates mentioned in the premise
if death_rate_hypothesis <= death_rate_premise:
    # check if the estimate of 'death_rate_hypothesis' contradicts the number of deaths in the premise
    label = "contradiction"
elif migration_rate_hypothesis != migration_rate_premise:
    # check if the migration rate in the hypothesis contradicts the migration rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

