# Define the variables for the premise
limes_alyssa = 25.0
limes_mike = 32.0
limes_tom = 12.0
total_limes = limes_alyssa + limes_mike + limes_tom

# Define the variables for the hypothesis
total_limes_hypothesis = 61.0

# Check if the total number of limes in the hypothesis contradicts the total number of limes from the premise
if total_limes_hypothesis!= total_limes:
    label = "contradiction"
else:
    label = "entailment"

print(label)
