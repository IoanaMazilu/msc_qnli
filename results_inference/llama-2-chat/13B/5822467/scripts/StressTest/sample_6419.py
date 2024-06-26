# Define variables with representative names for the numerical entities in both inputs
angel_gang_premise = 3
angel_gang_hypothesis = 7

# Extract all quantities as valid numbers (integers or floats)
ways_premise = angel_gang_premise * (angel_gang_premise + 1) // 2
ways_hypothesis = angel_gang_hypothesis * (angel_gang_hypothesis + 1) // 2

# Use brief comments to explain what comparison you do between the defined variables
# (do not use their values in the comments)

# Compare the number of ways to invite gang members to Angel's house
if ways_hypothesis <= ways_premise:
    # Check if the hypothesis value contradicts the estimate of the number of ways to invite gang members in the premise
    label = "contradiction"
elif ways_premise!= ways_hypothesis:
    # Check if the number of ways to invite gang members in the hypothesis contradicts the number of ways reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
