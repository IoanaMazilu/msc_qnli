# The hypothesis refers to the same situation as the premise, but with a different number of more minutes.
if x >= 15:
    # Check if the hypothesis value contradicts the premise value of 'x'
    label = "contradiction"
else:
    # If the hypothesis value is less than or equal to 'x', it is consistent with the premise
    label = "entailment"

print(label)
