john_ratio = 2
jose_ratio = 4
binoy_ratio = 6

premise_total = 6600
hypothesis_total = 0

# calculate the total amount of money among John, Jose, and Binoy in the given ratio
for i in range(3):
    amount = premise_total * i / (john_ratio + jose_ratio + binoy_ratio)
    hypothesis_total += amount

# check if the hypothesis value contradicts the estimate of the total amount in the premise
if hypothesis_total < premise_total:
    label = "contradiction"
elif hypothesis_total > premise_total:
    # the hypothesis value is consistent with the premise estimate
    label = "entailment"
else:
    # the premise estimate is not explicit enough to entail the hypothesis value
    label = "neutral"

print(label)
