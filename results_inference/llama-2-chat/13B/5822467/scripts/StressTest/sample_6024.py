% matplotlib inline

# Define variables with representative names for the numerical entities in both inputs
parents_amount_premise = 4 * 12  # 48 months x 12 months/year
parents_amount_hypothesis = 6 * 12  # 72 months x 12 months/year
dana_payments_premise = 4 % 12  # 4 months out of 12
dana_payments_hypothesis = less than 6 % 12  # less than 6 months out of 12

# Extract all quantities as valid numbers (integers or floats)
parents_amount_premise = int(parents_amount_premise)
parents_amount_hypothesis = int(parents_amount_hypothesis)
dana_payments_premise = int(dana_payments_premise)
dana_payments_hypothesis = int(dana_payments_hypothesis)

# Perform calculations if necessary
total_owed_premise = parents_amount_premise - dana_payments_premise
total_owed_hypothesis = parents_amount_hypothesis - dana_payments_hypothesis

# Compare the results
if dana_payments_hypothesis > dana_payments_premise:
    # The hypothesis refers to a lower number of payments than the premise, so we can infer entailment
    label = "entailment"
elif total_owed_hypothesis > total_owed_premise:
    # The hypothesis refers to a higher amount still owed after four years, so we can infer contradiction
    label = "contradiction"
else:
    # The premise and hypothesis values are consistent, so we can infer neutrality
    label = "neutral"

print(label)
