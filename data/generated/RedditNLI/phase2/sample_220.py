# Premise: Retail sales nationally drop 0.4% in January.
# Hypothesis: U.S. retail sales fall 0.4% in January.
# Golden Label: entailment

sales_drop_premise = 0.4
sales_drop_hypothesis = 0.4

# the hypothesis and premise mention the drop percentage of retail sales in January
if sales_drop_premise != sales_drop_hypothesis:
    # check if the drop percentage in the hypothesis contradicts the drop percentage in the premise
    label = "contradiction"
else:
    # if the drop percentage in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

