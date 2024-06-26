# Define variables with representative names for the numerical entities in both inputs
apples_maddie_premise = 88
apples_mike_premise = 12
apples_maddie_hypothesis = 18

# Extract all quantities as valid numbers (integers or floats)
apples_maddie_premise = int(apples_maddie_premise)
apples_mike_premise = int(apples_mike_premise)
apples_maddie_hypothesis = int(apples_maddie_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if apples_maddie_hypothesis <= apples_maddie_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'apples_maddie_premise'
    label = "contradiction"
elif apples_mike_premise!= apples_mike_hypothesis:
    # Check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
