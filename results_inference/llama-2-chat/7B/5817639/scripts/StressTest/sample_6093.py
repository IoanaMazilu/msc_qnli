# Define variables for the premise and hypothesis
premise_digits = 0
hypothesis_digits = 0

# Extract all digits from the premise and hypothesis
premise_digits = int(re.findall(r'\d+', premise))
hypothesis_digits = int(re.findall(r'\d+', hypothesis))

# Check if the hypothesis digits are less than or equal to the premise digits
if hypothesis_digits <= premise_digits:
    # Check if the hypothesis value contradicts the estimate of the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of digits
    # Any number of digits greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
