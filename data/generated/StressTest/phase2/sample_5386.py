# Premise: If there are less than 64 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Hypothesis: If there are 14 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Golden Label: neutral

more_supermarkets_US_premise = 64
more_supermarkets_US_hypothesis = 14

# the hypothesis talks about the number of more FGH supermarkets in the US than in Canada, referenced also in the premise
if more_supermarkets_US_hypothesis >= more_supermarkets_US_premise:
    # check if the hypothesis value contradicts the statement that there are less than 'more_supermarkets_US_premise'
    label = "contradiction"
else:
    # any number of more supermarkets in the US than in Canada, less than 'more_supermarkets_US_premise', is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

