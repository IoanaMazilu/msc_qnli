# Define variables for the premise and hypothesis
premise_p = 3
premise_less_than_3p_plus_1 = 1
hypothesis_p = 3
hypothesis_2p_plus_1 = 5

# Check if the hypothesis values and estimates do not contradict the premise ones
if hypothesis_p!= premise_p:
    label = "contradiction"
elif hypothesis_2p_plus_1!= premise_less_than_3p_plus_1:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
