ratio_premise = [2, 4, 8]
ratio_hypothesis = [1, 4, 8]

# the hypothesis refers to the ratio of money distribution between Priya, Mani and Rani
# the hypothesis value is less than the premise value for the first element of the ratio
if ratio_hypothesis[0] >= ratio_premise[0]:
    # check if the hypothesis value contradicts the premise value for the first element of the ratio
    label = "contradiction"
elif ratio_hypothesis[1]!= ratio_premise[1]:
    # check if the hypothesis value contradicts the premise value for the second element of the ratio
    label = "contradiction"
elif ratio_hypothesis[2]!= ratio_premise[2]:
    # check if the hypothesis value contradicts the premise value for the third element of the ratio
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
