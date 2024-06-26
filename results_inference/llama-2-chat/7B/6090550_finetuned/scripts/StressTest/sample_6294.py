ys_premise = 40
ys_hypothesis = 60

# the hypothesis refers to the percentage of money given to the wife mentioned in the premise
if ys_premise >= ys_hypothesis:
    # check if the percentage in the premise contradicts the percentage in the hypothesis
    label = "contradiction"
else:
    # if the percentage in the premise is less than the percentage in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
