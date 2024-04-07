# Premise: Bhanu spends 30% of his income on petrol on scooter 21% of the remaining on house rent and the balance on food.
# Hypothesis: Bhanu spends less than 50% of his income on petrol on scooter 21% of the remaining on house rent and the balance on food.
# Golden Label: entailment

petrol_expense_premise = 30
petrol_expense_hypothesis = 50

# the hypothesis refers to Bhanu's petrol expense which is also mentioned in the premise
if petrol_expense_hypothesis <= petrol_expense_premise:
    # check if the estimated 'petrol_expense_hypothesis' contradicts the petrol expense in the premise
    label = "entailment"
else:
    # if the hypothesis estimate is larger than the premise one, we have a contradiction
    label = "contradiction"

print(label)

