more_supermarkets_US_premise = 14
more_supermarkets_US_hypothesis = 54

# the hypothesis refers to the difference in the number of FGH supermarkets between US and Canada, mentioned in the premise
if more_supermarkets_US_hypothesis < more_supermarkets_US_premise:
    # check if the hypothesis contradicts the premise about the number of more supermarkets in the US
    label = "contradiction"
elif more_supermarkets_US_hypothesis > more_supermarkets_US_premise:
    # a greater number of more supermarkets in the US, as stated in the hypothesis, does not contradict the premise, but it cannot be directly entailed from it
    label = "neutral"
else:
    # if the numbers of more supermarkets in the US are equal in both premise and hypothesis, we can infer entailment
    label = "entailment"

print(label)
