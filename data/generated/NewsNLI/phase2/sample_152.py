# Premise: Two people died on the spot while third died while undergoing treatment at hospital.
# Hypothesis: Two people were killed on the spot, and another died at a hospital.
# Golden Label: entailment

people_died_spot_premise = 2
people_died_spot_hypothesis = 2
people_died_hospital_premise = 1
people_died_hospital_hypothesis = 1

# the hypothesis mentions the number of people died on the spot and at the hospital, which are also mentioned in the premise
if people_died_spot_hypothesis != people_died_spot_premise:
    # check if the number of people died on the spot in the hypothesis contradicts the number of people died on the spot in the premise
    label = "contradiction"
elif people_died_hospital_hypothesis != people_died_hospital_premise:
    # check if the number of people died at the hospital from the hypothesis contradicts the number of people died at the hospital in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

