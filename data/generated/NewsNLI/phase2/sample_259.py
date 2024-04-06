# Premise: Two people on the plane died at the crash scene, authorities said.
# Hypothesis: Two people on board died in the crash, authorities say.
# Golden Label: entailment

people_dead_premise = 2
people_dead_hypothesis = 2

# the hypothesis mentions the number of people who died on the plane, which is also mentioned in the premise
if people_dead_hypothesis != people_dead_premise:
    # check if the number of dead people in the hypothesis contradicts the number of dead people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

