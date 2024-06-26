petrol_spending_premise = 0.5
petrol_spending_hypothesis = 0.3
rent_spending_premise = 0.21
rent_spending_hypothesis = 0.21

# the hypothesis talks about the percentage of income Bhanu spends on petrol and rent, referenced also in the premise
if petrol_spending_hypothesis >= petrol_spending_premise:
    # check if the hypothesis value contradicts the estimate of less than 'petrol_spending_premise'
    label = "contradiction"
elif rent_spending_hypothesis != rent_spending_premise:
    # check if the percentage of rent spending in the hypothesis contradicts the percentage of rent spending reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of petrol spending
    # any percentage of petrol spending less than 'petrol_spending_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
