# Convert JPY to USD for comparison
jpy_trillion_premise = 0.93
jpy_trillion_hypothesis = 7.01

# Convert JPY to USD
usd_hypothesis = jpy_trillion_hypothesis / 100

# Compare the amounts in USD
if usd_hypothesis == jpy_trillion_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
