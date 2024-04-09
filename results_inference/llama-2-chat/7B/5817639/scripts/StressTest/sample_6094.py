# Define variables for the premise and hypothesis
premise_digits = []
hypothesis_digits = []

# Extract the digits from the premise and hypothesis
for i in range(10):
    premise_digits.append(int(input_text.split()[i]))
for i in range(10):
    hypothesis_digits.append(int(hypothesis_digits[i]))

# Check if the hypothesis digits contradict the premise digits
if hypothesis_digits[0] > premise_digits[0]:
    label = "contradiction"
elif any(hypothesis_digits[i] > premise_digits[i] for i in range(10)):
    label = "contradiction"
else:
    # If the hypothesis digits do not contradict the premise digits, we can infer entailment
    label = "entailment"

# Print the label
print(label)
