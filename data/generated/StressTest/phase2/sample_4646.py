# Premise: After the recall of defective by Telvin inc 2 years ago, its share price has since lost 12 %.
# Hypothesis: After the recall of defective by Telvin inc 6 years ago, its share price has since lost 12 %.
# Golden Label: contradiction

recall_years_premise = 2
recall_years_hypothesis = 6
share_price_loss = 12

# The hypothesis refers to the time of recall and share price loss mentioned in the premise
if recall_years_hypothesis != recall_years_premise:
    # check if the time of recall in the hypothesis contradicts the time of recall reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

