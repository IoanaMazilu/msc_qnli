death_rate_premise = 10
death_rate_hypothesis = 30
migration_rate_premise = 20
migration_rate_hypothesis = 20

# the hypothesis refers to the rates of death and migration in the village mentioned in the premise
if death_rate_premise >= death_rate_hypothesis:
    # check if the estimate of 'death_rate_hypothesis' contradicts the death rate in the premise
    label = "contradiction"
elif migration_rate_hypothesis!= migration_rate_premise:
    # check if the migration rate in the hypothesis contradicts the migration rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
