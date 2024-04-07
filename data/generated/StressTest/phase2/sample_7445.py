# Premise: Bhanu spends 30% of his income on petrol on scooter 14% of the remaining on house rent and the balance on food.
# Hypothesis: Bhanu spends more than 30% of his income on petrol on scooter 14% of the remaining on house rent and the balance on food.
# Golden Label: contradiction

income_petrol_premise = 30
income_petrol_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, mentioned in the premise
if income_petrol_hypothesis <= income_petrol_premise:
    # check if the estimate of 'income_petrol_hypothesis' contradicts the percentage of income on petrol in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

