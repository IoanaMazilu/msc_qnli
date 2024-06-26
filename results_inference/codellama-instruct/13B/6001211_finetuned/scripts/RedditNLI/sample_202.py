error_premise = 2 * 10**12
error_hypothesis = 2 * 10**12

# the hypothesis and premise mention a budget error of $2 trillion
if error_hypothesis!= error_premise:
    # check if the error amount in the hypothesis contradicts the error amount in the premise
    label = "contradiction"
else:
    # if the error amount in the hypothesis does not contradict the error amount in the premise, we can infer entailment
    label = "entailment"

print(label)
