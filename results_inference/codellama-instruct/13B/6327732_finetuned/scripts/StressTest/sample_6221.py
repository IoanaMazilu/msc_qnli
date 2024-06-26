premise_ratio = [2, 4, 8]
hypothesis_ratio = [1, 4, 8]

# the hypothesis refers to the ratio of money distribution between Priya, Mani and Rani
if hypothesis_ratio[0] < premise_ratio[0]:
    # check if the hypothesis value contradicts the premise ratio
    label = "contradiction"
elif hypothesis_ratio[1]!= premise_ratio[1]:
    # check if the hypothesis value contradicts the premise ratio
    label = "contradiction"
elif hypothesis_ratio[2]!= premise_ratio[2]:
    # check if the hypothesis value contradicts the premise ratio
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
