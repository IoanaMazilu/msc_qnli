error_premise = 2
error_hypothesis = 2

# the hypothesis and premise mention a numerical error in the budget
if error_hypothesis!= error_premise:
    # check if the error in the hypothesis contradicts the error in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
