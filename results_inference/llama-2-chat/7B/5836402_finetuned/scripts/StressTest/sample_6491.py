borrowed_premise = 6500
borrowed_hypothesis = 1500

# the hypothesis refers to the amount borrowed by Dana for her college education mentioned in the premise
if borrowed_hypothesis!= borrowed_premise:
    # check if the borrowed amount in the hypothesis contradicts the borrowed amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
