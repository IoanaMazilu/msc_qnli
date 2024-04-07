# Premise: In a BCCI meeting there are 15 people.
# Hypothesis: In a BCCI meeting there are 35 people.
# Golden Label: contradiction

people_premise = 15
people_hypothesis = 35

# the hypothesis refers to the number of people in a BCCI meeting mentioned in the premise
if people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

