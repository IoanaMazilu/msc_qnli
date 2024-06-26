y_premise = 50
y_hypothesis = 20

# the hypothesis refers to the percentage of students with cars, which is also mentioned in the premise
if y_hypothesis >= y_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis is less than the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
