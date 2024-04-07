# Premise: Bhanu spends 30% of his income on petrol on scooter 30% of the remaining on house rent and the balance on food.
# Hypothesis: Bhanu spends more than 30% of his income on petrol on scooter 30% of the remaining on house rent and the balance on food.
# Golden Label: contradiction

petrol_expense_premise = 0.30
petrol_expense_hypothesis = 0.30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_expense_hypothesis > petrol_expense_premise:
    # check if the percentage in the hypothesis contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)

