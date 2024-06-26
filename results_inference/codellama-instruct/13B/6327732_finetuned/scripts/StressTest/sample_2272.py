# define variables for the premise and hypothesis
premise_ratio = 4/3
hypothesis_ratio = 2/3

# check if the hypothesis ratio contradicts the premise ratio
if hypothesis_ratio >= premise_ratio:
    label = "contradiction"
else:
    label = "neutral"

print(label)
