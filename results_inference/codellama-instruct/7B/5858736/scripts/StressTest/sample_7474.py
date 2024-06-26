# Define variables for the premise and hypothesis
premise_p = 200
premise_less_than_4p_plus_1 = 15
hypothesis_p = 100
hypothesis_2p_plus_1 = 15

# Check if the hypothesis values and estimates do not contradict the premise ones
if hypothesis_p <= premise_p and hypothesis_2p_plus_1 <= premise_less_than_4p_plus_1:
    label = "entailment"
else:
    label = "contradiction"

print(label)
