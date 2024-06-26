# Define variables for the premise and hypothesis
premise_speed = 2
hypothesis_speed = 5

# Calculate the number of miles walked by Sam
sam_miles = hypothesis_speed * (premise_speed / hypothesis_speed)

# Check if the hypothesis is entailed from the premise
if sam_miles > premise_speed:
    label = "entailment"
else:
    label = "contradiction"

print(label)
