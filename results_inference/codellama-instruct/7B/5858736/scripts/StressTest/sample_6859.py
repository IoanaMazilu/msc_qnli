# Define variables for the numerical entities in the premise and hypothesis
premise_distance = 3
premise_time = 1.25
hypothesis_distance = 4
hypothesis_time = 1.25

# Calculate the rate of walking for the premise
premise_rate = premise_distance / premise_time

# Calculate the rate of walking for the hypothesis
hypothesis_rate = hypothesis_distance / hypothesis_time

# Compare the rates of walking
if hypothesis_rate <= premise_rate:
    # The hypothesis rate is less than or equal to the premise rate, so the hypothesis is entailed
    label = "entailment"
else:
    # The hypothesis rate is greater than the premise rate, so the hypothesis is not entailed
    label = "contradiction"

print(label)
