# Premise: If there are 14 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Hypothesis: If there are less than 64 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Golden Label: entailment

supermarkets_difference_premise = 14
supermarkets_difference_hypothesis = 64

# the hypothesis talks about the difference in number of FGH supermarkets in the US and Canada, referenced also in the premise
if supermarkets_difference_hypothesis < supermarkets_difference_premise:
    # check if the hypothesis value contradicts the difference of 'supermarkets_difference_premise'
    label = "contradiction"
elif supermarkets_difference_hypothesis == supermarkets_difference_premise:
    # check if the hypothesis value equals to the difference of 'supermarkets_difference_premise'
    label = "entailment"
else:
    # the premise gives a specific difference in the number of FGH supermarkets
    # any difference greater than 'supermarkets_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

