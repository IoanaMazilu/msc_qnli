# Define variables with representative names for the numerical entities in both inputs
interest_premise = 8
interest_hypothesis = float(input("Enter the rate of interest (as a float): "))

# Extract all quantities as valid numbers (integers or floats)
if interest_hypothesis <= interest_premise:
    # Check if the estimate of 'interest_hypothesis' contradicts the premise
    label = "contradiction"
elif interest_premise!= interest_hypothesis:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
