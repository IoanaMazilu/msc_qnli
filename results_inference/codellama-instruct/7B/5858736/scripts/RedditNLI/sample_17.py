# Define variables for the numerical entities in the input
sensex_points = 500
tata_motors_points = 8.01
nifty_points = 0

# Extract all quantities as valid numbers
sensex_points = float(sensex_points)
tata_motors_points = float(tata_motors_points)
nifty_points = float(nifty_points)

# Perform calculations if necessary
total_points = sensex_points + tata_motors_points

# Compare the variables to infer one of the following:
# "entailment": the hypothesis can be fully and explicitly entailed from the premise
# "contradiction": at least one aspect in the hypothesis contradicts the premise
# "neutral": the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
if total_points < 0:
    label = "contradiction"
else:
    label = "neutral"

print(label)
