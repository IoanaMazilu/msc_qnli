# Define variables for the premise and hypothesis
premise_p = 20
premise_2p_1 = 20 + 1 = 21
premise_3p_1 = 30 + 1 = 31

hypothesis_p = 20
hypothesis_2p_1 = 20 + 1 = 21
hypothesis_3p_1 = 30 + 1 = 31

# Check if the hypothesis values and estimates do not contradict the premise ones
if hypothesis_p == premise_p and hypothesis_2p_1 == premise_2p_1 and hypothesis_3p_1 == premise_3p_1:
    label = "entailment"
else:
    label = "contradiction"

print(label)
