people_premise = 6
people_hypothesis = 5

# the hypothesis refers to the number of people being arranged, as mentioned in the premise
if people_premise != people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis does not contradict the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
