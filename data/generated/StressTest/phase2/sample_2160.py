# Premise: If there are 22 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Hypothesis: If there are less than 52 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Golden Label: entailment

supermarkets_difference_premise = 22
supermarkets_difference_hypothesis = 52

# the hypothesis refers to the number of FGH supermarkets difference between US and Canada mentioned in the premise
if supermarkets_difference_hypothesis < supermarkets_difference_premise:
    # check if the estimate of 'supermarkets_difference_hypothesis' contradicts the number of supermarkets difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

