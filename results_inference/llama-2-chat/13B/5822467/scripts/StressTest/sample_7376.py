shift_premise = 16 * 4 = 64
order_premise = 40 * 4 = 160

# the hypothesis refers to the number of shifts and the average orders per hour
shift_hypothesis = 4 + 16
order_hypothesis = 40 * (4 + 16)

# calculate the total earnings based on the premise
earnings_premise = shift_premise * order_premise

# calculate the total earnings based on the hypothesis
earnings_hypothesis = shift_hypothesis * order_hypothesis

# compare the total earnings
if earnings_hypothesis > earnings_premise:
    # the hypothesis implies a higher total earnings than the premise, so the label is contradiction
    label = "contradiction"
elif earnings_hypothesis < earnings_premise:
    # the hypothesis implies a lower total earnings than the premise, so the label is entailment
    label = "entailment"
else:
    # the hypothesis and premise have the same total earnings, so the label is neutral
    label = "neutral"

print(label)
