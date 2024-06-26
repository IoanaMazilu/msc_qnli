people_premise = 5
people_hypothesis = 5

# the hypothesis refers to the number of people that can be seated on a bench, which is also mentioned in the premise
if people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis does not contradict the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
