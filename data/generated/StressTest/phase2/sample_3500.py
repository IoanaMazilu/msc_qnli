# Premise: Bhanu spends 30% of his income on petrol on scooter 20% of the remaining on house rent and the balance on food.
# Hypothesis: Bhanu spends more than 30% of his income on petrol on scooter 20% of the remaining on house rent and the balance on food.
# Golden Label: contradiction

petrol_expense_premise = 30
petrol_expense_hypothesis = 30

# the hypothesis talks about the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_expense_hypothesis <= petrol_expense_premise:
    # check if the percentage of income spent on petrol in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

