# Premise: However, 55 percent of the sales representatives prefer to stay at Hotel XYZ and 45 percent prefer to stay at Hotel ABC.
# Hypothesis: However, 85 percent of the sales representatives prefer to stay at Hotel XYZ and 45 percent prefer to stay at Hotel ABC.
# Golden Label: contradiction

sales_rep_XYZ_premise = 55
sales_rep_XYZ_hypothesis = 85
sales_rep_ABC_premise = 45
sales_rep_ABC_hypothesis = 45

# the hypothesis talks about the percentage of sales representatives who prefer to stay at Hotel XYZ and Hotel ABC, which is also mentioned in the premise
if sales_rep_XYZ_hypothesis != sales_rep_XYZ_premise:
    # check if the percentage of sales representatives who prefer to stay at Hotel XYZ in the hypothesis contradicts with the percentage mentioned in the premise
    label = "contradiction"
elif sales_rep_ABC_hypothesis != sales_rep_ABC_premise:
    # check if the percentage of sales representatives who prefer to stay at Hotel ABC in the hypothesis contradicts with the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the percentage values in the hypothesis do not contradict with the percentage values in the premise, we have to check the entailment
    label = "entailment"

print(label)

