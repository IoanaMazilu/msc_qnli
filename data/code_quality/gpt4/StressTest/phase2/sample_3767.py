total_borrowed_premise = 6000
total_borrowed_hypothesis = 8000

# the hypothesis refers to the total borrowed amount mentioned in the premise
if total_borrowed_premise != total_borrowed_hypothesis:
    # check if the total borrowed amount mentioned in the hypothesis contradicts the total borrowed amount mentioned in the premise
    label = "contradiction"
else:
    # if the total borrowed amount in the hypothesis does not contradict the total borrowed amount in the premise, we can infer entailment
    label = "entailment"

print(label)
