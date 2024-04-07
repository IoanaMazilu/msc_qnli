# Premise: 5% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Hypothesis: less than 6% people of a village in Sri Lanka died by bombardment, 15% of the remainder left the village on account of fear.
# Golden Label: entailment

death_rate_premise = 5
death_rate_hypothesis = 6
migration_rate_premise = 15
migration_rate_hypothesis = 15

# the hypothesis refers to the rates of deaths and migrations mentioned in the premise
if death_rate_premise >= death_rate_hypothesis:
    # check if the death rate in the hypothesis contradicts the death rate in the premise
    label = "contradiction"
elif migration_rate_hypothesis != migration_rate_premise:
    # check if the migration rate in the hypothesis contradicts the migration rate in the premise
    label = "contradiction"
else:
    # if the hypothesis rates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

