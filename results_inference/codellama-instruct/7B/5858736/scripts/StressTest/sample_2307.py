# Define variables for the numerical entities in the premise and hypothesis
premise_anne_speed = 2
premise_cleaning_time = 6
hypothesis_anne_speed = 4
hypothesis_cleaning_time = 5

# Extract all quantities as valid numbers
premise_cleaning_time = float(premise_cleaning_time)
hypothesis_cleaning_time = float(hypothesis_cleaning_time)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_anne_speed <= premise_anne_speed:
    # Check if the hypothesis value contradicts the estimate of doubled speed in the premise
    label = "contradiction"
elif hypothesis_cleaning_time >= premise_cleaning_time:
    # Check if the hypothesis value contradicts the estimate of less than 5 hours in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
