premise_red = 4
premise_green = 3
premise_blue = 1

hypothesis_red = 3
hypothesis_green = 2
hypothesis_blue = 1

# check if the hypothesis values contradict the premise values
if hypothesis_red < premise_red or hypothesis_green < premise_green or hypothesis_blue < premise_blue:
    label = "contradiction"
# check if the hypothesis values are consistent with the premise values
elif hypothesis_red >= premise_red and hypothesis_green >= premise_green and hypothesis_blue >= premise_blue:
    label = "entailment"
# the hypothesis values are not consistent with the premise values, but cannot be explicitly entailed from the premise
else:
    label = "neutral"

print(label)
