# Define variables with representative names for the numerical entities in both inputs
amount_premise = 3
months_premise = 4
percentage_given_premise = 3
amount_given_premise = amount_premise * percentage_given_premise / 100
total_amount_given_premise = amount_given_premise * months_premise
amount_owed_premise = amount_premise - total_amount_given_premise

# Define variables with representative names for the numerical entities in the hypothesis
percentage_given_hypothesis = 3
amount_given_hypothesis = amount_premise * percentage_given_hypothesis / 100
total_amount_given_hypothesis = amount_given_hypothesis * months_premise
amount_owed_hypothesis = amount_premise - total_amount_given_hypothesis

# Check if the hypothesis value contradicts the estimate of more than 'amount_owed_premise'
if amount_owed_hypothesis <= amount_owed_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount owed
    # any number of dollars greater than 'amount_owed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
