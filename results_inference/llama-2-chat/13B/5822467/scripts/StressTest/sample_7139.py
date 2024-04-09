# Define variables with representative names for the numerical entities in both inputs
saving_amount_premise = Rs.10000 # premise: current balance
saving_amount_hypothesis = Rs.6000 # hypothesis: current balance
loan_payment_premise = 10 # premise: percentage of loan payment
loan_payment_hypothesis = 40 # hypothesis: percentage of loan payment

# Extract all quantities as valid numbers (integers or floats)
saving_amount_premise = float(saving_amount_premise)
saving_amount_hypothesis = float(saving_amount_hypothesis)
loan_payment_premise = float(loan_payment_premise)
loan_payment_hypothesis = float(loan_payment_hypothesis)

# Perform calculations if necessary
saving_amount_diff = saving_amount_hypothesis - saving_amount_premise
loan_payment_diff = loan_payment_hypothesis - loan_payment_premise

# Compare the variables using brief comments to explain what comparison you do
# (do not use their values in the comments)
if saving_amount_diff > 0:
    # The hypothesis suggests a greater decrease in the saving amount than the premise
    label = "contradiction"
elif loan_payment_diff > 0:
    # The hypothesis suggests a greater loan payment than the premise
    label = "contradiction"
else:
    # The hypothesis values and estimates do not contradict the premise ones
    label = "entailment"

print(label)
