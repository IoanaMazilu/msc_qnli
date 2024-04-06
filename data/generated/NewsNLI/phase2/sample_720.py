# Premise: Malaysian Maritime Enforcement Agency said 60 people have been rescued so far, and five bodies have been recovered.
# Hypothesis: 60 people rescued from sea.
# Golden Label: neutral

people_rescued_premise = 60
people_rescued_hypothesis = 60

# the hypothesis mentions the number of people rescued, which is also mentioned in the premise
if people_rescued_hypothesis != people_rescued_premise:
    # check if the number of people rescued in the hypothesis contradicts the number of people rescued reported in the premise
    label = "contradiction"
else:
    # if the number of people rescued in the hypothesis does not contradict the number of people rescued in the premise, we can infer entailment
    label = "entailment"

print(label)

