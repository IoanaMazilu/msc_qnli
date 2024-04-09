# Define variables with representative names for the numerical entities in both inputs
lucy_deposit_premise = float(22500)
lucy_deposit_hypothesis = float(62500)
annual_return_premise = 8 / 4  # calculate quarterly return from annual return
annual_return_hypothesis = 8 / 4

# Extract all quantities as valid numbers
if lucy_deposit_hypothesis > lucy_deposit_premise:
    # Check if the hypothesis value contradicts the premise estimate
    label = "contradiction"
elif annual_return_hypothesis!= annual_return_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
