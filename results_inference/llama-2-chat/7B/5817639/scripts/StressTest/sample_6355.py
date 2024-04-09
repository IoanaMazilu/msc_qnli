# Variables for premise and hypothesis
microTron_premise = 76
microTron_hypothesis = 36
dynaco_premise = 48
dynaco_hypothesis = 48

# Calculate the average price per share
average_price = (microTron_premise + dynaco_premise) / 300

# Check if the hypothesis contradicts the premise
if microTron_hypothesis > microTron_premise:
    label = "contradiction"
elif dynaco_hypothesis > dynaco_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

# Print the label
print(label)
