# Define variables for the premise and hypothesis
premise_p = 20
premise_2p_1 = 20 + 1 = 21
hypothesis_p = 21
hypothesis_2p_1 = 21 + 1 = 22

# Check if the hypothesis values and estimates do not contradict the premise ones
if hypothesis_2p_1 <= premise_2p_1:
    label = "entailment"
else:
    label = "contradiction"

print(label)
