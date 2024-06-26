premise_ratio = [4, 4, 8]
hypothesis_ratio = [2, 4, 8]

# check if the hypothesis ratio contradicts the premise ratio
if hypothesis_ratio[0] < premise_ratio[0]:
    label = "contradiction"
elif hypothesis_ratio[1] > premise_ratio[1]:
    label = "contradiction"
elif hypothesis_ratio[2] > premise_ratio[2]:
    label = "contradiction"
else:
    label = "neutral"

print(label)
