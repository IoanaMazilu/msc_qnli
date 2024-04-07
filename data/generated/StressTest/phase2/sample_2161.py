# Premise: If there are less than 52 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Hypothesis: If there are 22 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Golden Label: neutral

supermarkets_difference_premise = 52
supermarkets_difference_hypothesis = 22

# the hypothesis refers to the difference in the number of FGH supermarkets in the US and Canada mentioned in the premise
if supermarkets_difference_hypothesis > supermarkets_difference_premise:
    # check if the difference in the hypothesis contradicts the upper limit of the difference in the premise
    label = "contradiction"
elif supermarkets_difference_hypothesis == supermarkets_difference_premise:
    # check if the difference in the hypothesis is the same as the upper limit of the difference in the premise
    label = "entailment"
else:
    # the premise gives only an upper limit for the difference in the number of supermarkets
    # any difference less than 'supermarkets_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

