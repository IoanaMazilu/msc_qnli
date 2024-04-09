problems_premise = 30
problems_hypothesis = 70

# the hypothesis talks about the range of problems solved by Andy in a Math exercise
if problems_hypothesis <= problems_premise:
    # check if the hypothesis value contradicts the estimate of the range of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the range of problems solved, and the hypothesis value falls within that range, so we can infer entailment
    label = "entailment"

print(label)
