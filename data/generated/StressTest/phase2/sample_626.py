# Premise: Ahok will arrange 6 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Hypothesis: Ahok will arrange 2 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Golden Label: contradiction

people_premise = 6
people_hypothesis = 2

# the hypothesis refers to the number of people mentioned in the premise
if people_premise != people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

