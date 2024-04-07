# Premise: If there are 22 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Hypothesis: If there are 42 more FGH supermarkets in the US than in Canada, how many FGH supermarkets are there in the US?
# Golden Label: contradiction

more_supermarkets_us_premise = 22
more_supermarkets_us_hypothesis = 42

# the hypothesis refers to the difference in the number of FGH supermarkets between the US and Canada mentioned in the premise
if more_supermarkets_us_hypothesis != more_supermarkets_us_premise:
    # check if the difference in the number of supermarkets in the hypothesis contradicts the difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

