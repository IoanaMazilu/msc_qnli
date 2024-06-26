y_premise = 0.2
y_hypothesis = 0.5

# the hypothesis refers to the percentage of students with cars, which is also mentioned in the premise
if y_premise!= y_hypothesis:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage of students with cars in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
