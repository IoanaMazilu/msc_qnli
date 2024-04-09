# Define variables with representative names for the numerical entities in both inputs
investment_premise = 8000
interest_rate_premise = 5
time_premise = 2

# Extract all quantities as valid numbers (integers or floats)
investment_hypothesis = 2000
interest_rate_hypothesis = 5
time_hypothesis = 2

# Perform calculations if necessary
interest_premise = investment_premise * (1 + interest_rate_premise/100) ** time_premise
interest_hypothesis = investment_hypothesis * (1 + interest_rate_hypothesis/100) ** time_hypothesis

# Compare the variables
if investment_hypothesis <= interest_premise:
    # Check if the hypothesis value contradicts the amount of interest earned in the premise
    label = "contradiction"
elif interest_hypothesis!= interest_premise:
    # Check if the amount of interest earned in the hypothesis contradicts the amount of interest earned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
