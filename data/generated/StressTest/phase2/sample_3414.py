# Premise: 30% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Hypothesis: less than 50% people of a village in Sri Lanka died by bombardment, 25% of the remainder left the village on account of fear.
# Golden Label: entailment

death_rate_premise = 30
death_rate_hypothesis = 50
migration_rate_premise = 25
migration_rate_hypothesis = 25

# the hypothesis talks about the death and migration rates, mentioned also in the premise
if death_rate_hypothesis > death_rate_premise:
    # check if the hypothesis value contradicts the death rate in the premise
    label = "contradiction"
elif migration_rate_premise != migration_rate_hypothesis:
    # check if the migration rate in the hypothesis contradicts the migration rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

