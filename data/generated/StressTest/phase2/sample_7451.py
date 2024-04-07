# Premise: Bhanu spends 30% of his income on petrol on scooter 12% of the remaining on house rent and the balance on food.
# Hypothesis: Bhanu spends more than 30% of his income on petrol on scooter 12% of the remaining on house rent and the balance on food.
# Golden Label: contradiction

petrol_expense_premise = 30
petrol_expense_hypothesis = 30

# the hypothesis talks about the percentage of income Bhanu spends on petrol, referenced also in the premise
if petrol_expense_hypothesis <= petrol_expense_premise:
    # if the percentage in the hypothesis is less than or equal to the one in the premise, it contradicts the "more than" claim in the hypothesis
    label = "contradiction"
else:
    # any percentage greater than 'petrol_expense_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

