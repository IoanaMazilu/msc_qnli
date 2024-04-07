# Premise: If there are 14 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Hypothesis: If there are less than 74 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Golden Label: entailment

more_supermarkets_US_premise = 14
more_supermarkets_US_hypothesis = 74

# the hypothesis refers to the difference in number of FGH supermarkets between US and Canada
if more_supermarkets_US_premise >= more_supermarkets_US_hypothesis:
    # check if the premise number contradicts the hypothesis that states there are less than 'more_supermarkets_US_hypothesis'
    label = "contradiction"
elif more_supermarkets_US_premise < more_supermarkets_US_hypothesis:
    # if the premise number is less than the hypothesis value, it does not contradict it
    # but the specific number of supermarkets in the US cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)

