# Premise: The quakes have displaced some 14,000 people, the civil protection agency said.
# Hypothesis: Some 14,000 people have been displaced by the quakes, the agency says.
# Golden Label: entailment

displaced_people_premise = 14000
displaced_people_hypothesis = 14000

# the hypothesis mentions the number of people displaced by the quakes, which is also mentioned in the premise
if displaced_people_hypothesis != displaced_people_premise:
    # check if the number of displaced people in the hypothesis contradicts the number of displaced people reported in the premise
    label = "contradiction"
else:
    # if the number of displaced people in the hypothesis does not contradict the number of displaced people in the premise, we can infer entailment
    label = "entailment"

print(label)

