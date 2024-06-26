petrol_percentage_premise = 30
petrol_percentage_hypothesis = 30
house_rent_percentage_premise = 12
house_rent_percentage_hypothesis = 12

# the hypothesis refers to the percentage of income spent on petrol and house rent, mentioned in the premise
if petrol_percentage_hypothesis <= petrol_percentage_premise:
    # check if the estimate of 'petrol_percentage_hypothesis' contradicts the percentage of petrol spending in the premise
    label = "contradiction"
elif house_rent_percentage_hypothesis!= house_rent_percentage_premise:
    # check if the percentage of house rent spending in the hypothesis contradicts the percentage of house rent spending reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
