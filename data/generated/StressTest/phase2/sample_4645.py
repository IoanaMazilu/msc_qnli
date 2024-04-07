# Premise: After the recall of defective by Telvin inc less than 4 years ago, its share price has since lost 12 %.
# Hypothesis: After the recall of defective by Telvin inc 2 years ago, its share price has since lost 12 %.
# Golden Label: neutral

recall_years_ago_premise = 4
recall_years_ago_hypothesis = 2
share_price_loss = 12 # this value is the same in both the premise and the hypothesis

# the hypothesis talks about the recall of defective by Telvin inc and the loss in share price, both referenced also in the premise
if recall_years_ago_hypothesis >= recall_years_ago_premise:
    # check if the hypothesis value contradicts the estimate of less than 'recall_years_ago_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years ago
    # any number of years less than 'recall_years_ago_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

