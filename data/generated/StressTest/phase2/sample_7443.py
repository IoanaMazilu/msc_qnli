# Premise: Bhanu spends 30% of his income on petrol on scooter 14% of the remaining on house rent and the balance on food.
# Hypothesis: Bhanu spends less than 60% of his income on petrol on scooter 14% of the remaining on house rent and the balance on food.
# Golden Label: entailment

petrol_expense_premise = 30
petrol_expense_hypothesis = 60

# the hypothesis talks about the percentage of income spent on petrol, which is also mentioned in the premise
if petrol_expense_premise >= petrol_expense_hypothesis:
    # check if the hypothesis estimate contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

