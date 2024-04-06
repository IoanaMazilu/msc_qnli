# Premise: At least three people have been killed and 52 injured after Buddhist mobs rampaged through Muslim areas in southwest Sri Lanka, police say.
# Hypothesis: At least 3 people dead, 52 injured after Buddhist mobs attacked Muslim areas in Sri Lanka.
# Golden Label: entailment

people_killed_premise = 3
people_injured_premise = 52
people_killed_hypothesis = 3
people_injured_hypothesis = 52

# the hypothesis mentions the minimum number of people killed and injured, which are also mentioned in the premise
if people_killed_hypothesis != people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif people_injured_hypothesis != people_injured_premise:
    # check if the number of people injured from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

