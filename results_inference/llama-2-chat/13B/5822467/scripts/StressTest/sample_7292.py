premise_amount = 600
hypothesis_amount = 400

# define variables for the numerical entities in the premise and hypothesis
gregs_share_premise = "Rs." + str(premise_amount)
gregs_share_hypothesis = "Rs." + str(hypothesis_amount)

# compare the variables to determine the label
if hypothesis_amount > premise_amount:
    label = "contradiction"
elif gregs_share_hypothesis!= gregs_share_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
