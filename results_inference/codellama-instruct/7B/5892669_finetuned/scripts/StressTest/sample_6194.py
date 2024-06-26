pay_premise = 150
pay_hypothesis = 150

# the hypothesis refers to the daily pay of Lexi's new job mentioned in the premise
if pay_hypothesis >= pay_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"

print(label)
