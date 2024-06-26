# define variables for the numerical entities in the premise and hypothesis
premise_amount = 5.12
hypothesis_amount = 1000

# check if the amount in the hypothesis contradicts the amount in the premise
if hypothesis_amount < premise_amount:
    label = "contradiction"
else:
    label = "neutral"

print(label)
