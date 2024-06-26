y_premise = 20
y_hypothesis = 50

# the hypothesis refers to the percentage of students with cars at Morse, mentioned in the premise
if y_premise >= y_hypothesis:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage of students with cars in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
