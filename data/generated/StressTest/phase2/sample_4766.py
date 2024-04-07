# Premise: Bhanu spends 30% of his income on petrol on scooter 10% of the remaining on house rent and the balance on food.
# Hypothesis: Bhanu spends less than 30% of his income on petrol on scooter 10% of the remaining on house rent and the balance on food.
# Golden Label: contradiction

petrol_spending_premise = 30
petrol_spending_hypothesis = 30

# the hypothesis talks about the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_spending_hypothesis >= petrol_spending_premise:
    # check if the hypothesis value contradicts the estimate of less than 'petrol_spending_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
