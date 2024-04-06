# Premise: U.S. retail sales fall 0.4% in January.
# Hypothesis: Retail sales nationally drop 0.4% in January.
# Golden Label: entailment

retail_sales_fall_premise = 0.4
retail_sales_drop_hypothesis = 0.4

# the hypothesis and premise mention the percentage of retail sales drop in January
if retail_sales_fall_premise != retail_sales_drop_hypothesis:
    # check if the percentage of drop in the hypothesis contradicts the percentage of drop in the premise
    label = "contradiction"
else:
    # if the percentage of drop in the hypothesis does not contradict the percentage of drop in the premise, we can infer entailment
    label = "entailment"

print(label)

