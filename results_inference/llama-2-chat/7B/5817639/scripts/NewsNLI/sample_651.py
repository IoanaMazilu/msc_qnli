# Define variables for premise and hypothesis
premise_amount = 5000000
hypothesis_amount = 5000000

# Check if the amount offered in the hypothesis contradicts the amount offered in the premise
if hypothesis_amount!= premise_amount:
    label = "contradiction"
elif hypothesis_amount < premise_amount:
    # If the amount offered in the hypothesis is less than the amount offered in the premise, it does not entail or contradict
    label = "neutral"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
