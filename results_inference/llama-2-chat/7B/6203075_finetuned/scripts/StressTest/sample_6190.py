save_days_premise = 80
save_days_hypothesis = 30

# the hypothesis refers to the number of days Lexi needs to save for a vacation, which is also mentioned in the premise
if save_days_hypothesis >= save_days_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"

print(label)
