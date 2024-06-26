# Define variables with representative names for the numerical entities in both inputs
days_needed_premise = 30
daily_wage_premise = 125
days_needed_hypothesis = 80

# Extract all quantities as valid numbers
days_needed_premise = int(days_needed_premise)
daily_wage_premise = int(daily_wage_premise)
days_needed_hypothesis = int(days_needed_hypothesis)

# Calculate the total amount needed to save for the vacation
total_amount_premise = days_needed_premise * daily_wage_premise

# Calculate the total amount needed to save for the vacation in the hypothesis
total_amount_hypothesis = days_needed_hypothesis * daily_wage_premise

# Compare the total amounts needed to save for the vacation in the premise and the hypothesis
if total_amount_premise <= total_amount_hypothesis:
    # The hypothesis value contradicts the total amount needed to save for the vacation in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of days needed to save for the vacation
    # Any number of days greater than 'days_needed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
