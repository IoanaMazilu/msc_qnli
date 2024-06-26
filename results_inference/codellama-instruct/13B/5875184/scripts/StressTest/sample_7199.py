premise_side_bc = 3
premise_side_ca = 4
premise_side_ab = 5

hypothesis_side_bc = 7
hypothesis_side_ca = 4
hypothesis_side_ab = 5

# check if the hypothesis values contradict the premise values
if hypothesis_side_bc < premise_side_bc:
    label = "contradiction"
elif hypothesis_side_ca < premise_side_ca:
    label = "contradiction"
elif hypothesis_side_ab < premise_side_ab:
    label = "contradiction"
else:
    label = "neutral"

print(label)
