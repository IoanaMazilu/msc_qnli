# the hypothesis and premise both use the same numbers
difference = hypothesis_amount - premise_amount

# the difference is calculated using the same numbers in both the premise and the hypothesis
if difference < 0.05:
    # if the difference is less than 0.05, it is likely that the hypothesis and premise are entailing the same amount
    label = "entailment"
elif difference >= 0.05:
    # if the difference is greater than or equal to 0.05, it is likely that the hypothesis and premise are contradicting each other
    label = "contradiction"
else:
    # if the difference is exactly 0.05, it is likely that the hypothesis and premise are neutral (no contradiction or entailment)
    label = "neutral"

print(label)
