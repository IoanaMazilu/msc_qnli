# Define variables with representative names for the numerical entities in both inputs
apples_premise = 9.0
erasers_premise = 12.0
friends_premise = 3.0

# Extract all quantities as valid numbers
apples_per_friend = apples_premise / friends_premise

# Use brief comments to explain what comparison you do between the defined variables
# Check if the number of apples per friend from the hypothesis contradicts the estimate of 3.0 apples per friend
if apples_per_friend!= 3.0:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
