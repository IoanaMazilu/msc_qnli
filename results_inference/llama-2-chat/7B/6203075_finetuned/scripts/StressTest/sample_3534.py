# the hypothesis refers to the number of t-shirts bought by Sanoop, which is also mentioned in the premise
label = "entailment"

# the hypothesis value is greater than the premise value
if t_shirts_bought_hypothesis <= t_shirts_bought_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
