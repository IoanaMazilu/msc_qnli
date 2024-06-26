petrol_spending_premise = 30
petrol_spending_hypothesis = 80
scooter_rent_premise = 12
scooter_rent_hypothesis = 12

# the hypothesis refers to the percentage of income Bhanu spends on petrol and scooter rent, mentioned in the premise
if petrol_spending_hypothesis <= petrol_spending_premise:
    # check if the estimate of 'petrol_spending_hypothesis' contradicts the percentage of petrol spending in the premise
    label = "contradiction"
elif scooter_rent_hypothesis!= scooter_rent_premise:
    # check if the percentage of scooter rent in the hypothesis contradicts the percentage of scooter rent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
