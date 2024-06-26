rate_hypothesis = 675
rate_premise = 375

if rate_hypothesis <= rate_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
