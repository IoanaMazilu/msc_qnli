# Premise: Bhanu spends less than 60% of his income on petrol on scooter 30% of the remaining on house rent and the balance on food.
# Hypothesis: Bhanu spends 30% of his income on petrol on scooter 30% of the remaining on house rent and the balance on food.
# Golden Label: neutral

income_spent_petrol_premise = 60
income_spent_petrol_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, mentioned in the premise
if income_spent_petrol_hypothesis >= income_spent_petrol_premise:
    # check if the percentage in the hypothesis contradicts the estimate of less than 'income_spent_petrol_premise' percentage in the premise
    label = "contradiction"
else:
    # any percentage less than 'income_spent_petrol_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

