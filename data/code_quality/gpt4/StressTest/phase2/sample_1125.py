more_fgh_supermarkets_us_premise = 10
more_fgh_supermarkets_us_hypothesis = 60

# the hypothesis refers to the number of FGH supermarkets in the US more than in Canada mentioned in the premise
if more_fgh_supermarkets_us_hypothesis < more_fgh_supermarkets_us_premise:
    # check if the hypothesis value contradicts the number of more FGH supermarkets in the US than in Canada in the premise
    label = "contradiction"
elif more_fgh_supermarkets_us_hypothesis == more_fgh_supermarkets_us_premise:
    # check if the hypothesis value is the same as the number of more FGH supermarkets in the US than in Canada in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, and are not the same, we can infer neutrality
    label = "neutral"

print(label)
