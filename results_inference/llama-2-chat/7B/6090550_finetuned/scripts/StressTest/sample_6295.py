ys_premise = 60
ys_hypothesis = 40

# the hypothesis talks about the percentage of money Jones gave to his wife, which is also mentioned in the premise
if ys_hypothesis >= ys_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
