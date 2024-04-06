# Premise: Pedestrians and shoppers died, and three officers were among more than two dozen people injured, said government official Javid Marwat and Peshawar Police Chief Tahir Ayub.
# Hypothesis: Explosion also injures more than two dozen people.
# Golden Label: neutral

injured_people_premise = 24
injured_people_hypothesis = 24

# the hypothesis mentions the number of people injured, which is also referenced in the premise
if injured_people_hypothesis != injured_people_premise:
    # check if the number of injured people in the hypothesis contradicts the number of injured people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

