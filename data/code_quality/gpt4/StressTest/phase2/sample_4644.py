recall_years_premise = 2
recall_years_hypothesis = 4
share_price_loss = 12 # Both premise and hypothesis report the same share price loss

# The hypothesis refers to the same event of the product recall by Telvin inc, and the subsequent share price loss
if recall_years_hypothesis < recall_years_premise:
    # Check if the hypothesis contradicts the premise by asserting that the recall occurred less than 'recall_years_premise' years ago
    label = "contradiction"
elif recall_years_hypothesis > recall_years_premise:
    # The premise gives the exact number of years since the recall
    # Any number of years greater than 'recall_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # If the recall years and share price loss in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
