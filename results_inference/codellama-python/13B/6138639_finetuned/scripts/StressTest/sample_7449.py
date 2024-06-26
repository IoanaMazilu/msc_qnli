petrol_percentage_premise = 30
petrol_percentage_hypothesis = 80

# the hypothesis refers to the percentage of income spent on petrol, which is also mentioned in the premise
if petrol_percentage_premise >= petrol_percentage_hypothesis:
    # check if the percentage of petrol spending in the premise contradicts the hypothesis estimate of less than 'petrol_percentage_hypothesis'
    label = "contradiction"
else:
    # if the premise percentage does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
