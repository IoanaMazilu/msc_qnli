y_premise = 25
y_hypothesis = 35

# The hypothesis refers to the efficiency ratio between Suresh and Kamal mentioned in the premise
if y_premise >= y_hypothesis:
    # check if the efficiency ratio in the hypothesis contradicts the efficiency ratio in the premise
    label = "contradiction"
else:
    # if the efficiency ratio in the hypothesis is less than the efficiency ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
