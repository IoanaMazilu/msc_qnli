death_rate_premise = 5
death_rate_hypothesis = 2
migration_rate_premise = 15
migration_rate_hypothesis = 15

# the hypothesis refers to the percentage of people who died and people who left the village as mentioned in the premise
if death_rate_hypothesis >= death_rate_premise:
    # check if the hypothesis death rate contradicts the death rate in the premise
    label = "contradiction"
elif migration_rate_hypothesis != migration_rate_premise:
    # check if the migration rate in the hypothesis contradicts the migration rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
