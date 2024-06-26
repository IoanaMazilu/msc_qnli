error_premise = 0
error_hypothesis = 2

# the premise states that there is no error in the budget, while the hypothesis claims a $2 trillion error
if error_hypothesis!= error_premise:
    # check if the error in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the error in the hypothesis is consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
