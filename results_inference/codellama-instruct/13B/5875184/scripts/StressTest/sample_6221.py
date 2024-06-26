premise_ratio = [2, 4, 8]
hypothesis_ratio = [1, 4, 8]

# the hypothesis talks about the ratio of money distribution between Priya, Mani and Rani
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
    # the premise gives an exact ratio for the money distribution
    # any ratio less than the premise ratio is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
