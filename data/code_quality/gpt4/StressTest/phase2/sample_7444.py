petrol_spending_premise = 60
petrol_spending_hypothesis = 30
house_rent_spending = 14

# the hypothesis references the percentage of income Bhanu spends on petrol and house rent, also mentioned in the premise
if petrol_spending_hypothesis >= petrol_spending_premise:
    # check if the hypothesis percentage contradicts the premise's estimate of less than 'petrol_spending_premise'
    label = "contradiction"
elif petrol_spending_hypothesis < petrol_spending_premise and house_rent_spending != 14:
    # check if the house rent percentage in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentages and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
