# Premise: If there are 14 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Hypothesis: If there are 24 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Golden Label: contradiction

supermarkets_diff_premise = 14
supermarkets_diff_hypothesis = 24

# the hypothesis refers to the difference of supermarkets in US and Canada mentioned in the premise
if supermarkets_diff_premise != supermarkets_diff_hypothesis:
    # check if the difference in the hypothesis contradicts the difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

