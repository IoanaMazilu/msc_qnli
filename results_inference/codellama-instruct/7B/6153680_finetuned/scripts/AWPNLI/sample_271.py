# Define variables for the premise
candy_scored = 47.0
candy_ate = 25.0
candy_given = 40.0

# Define variables for the hypothesis
total_candy = 65.0

# Calculate the total candy Faye has
total_candy_premise = candy_scored + candy_ate + candy_given

# Check if the total candy in the hypothesis contradicts the total candy from the premise
if total_candy!= total_candy_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
