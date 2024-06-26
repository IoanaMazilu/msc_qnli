# Extract numerical information from the input
payrolls_premise = 164,000
jobless_rate_premise = 3.9%

# Extract numerical information from the hypothesis
payrolls_hypothesis = 164,000
jobless_rate_hypothesis = 3.9%

# Check if the payrolls and jobless rate in the hypothesis contradict the premise
if payrolls_hypothesis!= payrolls_premise:
    label = "contradiction"
elif jobless_rate_hypothesis!= jobless_rate_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
