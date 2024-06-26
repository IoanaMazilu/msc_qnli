borrowed_premise = 6500
borrowed_hypothesis = 3500

# the hypothesis refers to the amount of money borrowed by Dana for her college education, which is also mentioned in the premise
if borrowed_hypothesis >= borrowed_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
