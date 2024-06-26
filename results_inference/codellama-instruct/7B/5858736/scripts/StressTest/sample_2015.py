# Define variables for the numerical entities in both inputs
loss_indu_premise = 0
loss_indu_hypothesis = 0
interest_rate_premise = 0
interest_rate_hypothesis = 0
time_period_premise = 0
time_period_hypothesis = 0

# Extract all quantities as valid numbers
loss_indu_premise = float(input("Enter the loss suffered by Indu: "))
interest_rate_premise = float(input("Enter the interest rate for 2 years: "))
time_period_premise = float(input("Enter the time period for 2 years: "))
loss_indu_hypothesis = float(input("Enter the loss suffered by Indu for 8 years: "))
interest_rate_hypothesis = float(input("Enter the interest rate for 8 years: "))
time_period_hypothesis = float(input("Enter the time period for 8 years: "))

# Calculate the simple interest for both time periods
simple_interest_premise = (loss_indu_premise * interest_rate_premise * time_period_premise) / 100
simple_interest_hypothesis = (loss_indu_hypothesis * interest_rate_hypothesis * time_period_hypothesis) / 100

# Compare the simple interests
if simple_interest_hypothesis <= simple_interest_premise:
    # Check if the estimate of'simple_interest_hypothesis' contradicts the simple interest in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
