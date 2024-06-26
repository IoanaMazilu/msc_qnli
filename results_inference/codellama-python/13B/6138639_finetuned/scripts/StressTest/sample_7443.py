petrol_percentage_premise = 30
petrol_percentage_hypothesis = 60

# the hypothesis refers to the percentage of income spent on petrol, which is also mentioned in the premise
if petrol_percentage_premise >= petrol_percentage_hypothesis:
    # check if the estimate of 'petrol_percentage_hypothesis' contradicts the percentage of petrol spending in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
