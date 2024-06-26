earn_less_than_50k_premise = 60
earn_less_than_50k_hypothesis = 20
earn_more_than_40k_premise = 60
earn_more_than_40k_hypothesis = 60
earn_43k_premise = 11
earn_43k_hypothesis = 11
earn_49k_premise = 5
earn_49k_hypothesis = 5

# the hypothesis refers to the earning of the employees in Lulu company mentioned in the premise
if earn_less_than_50k_premise < earn_less_than_50k_hypothesis:
    # check if the estimate of 'earn_less_than_50k_hypothesis' contradicts the percentage of employees earning less than 50k in the premise
    label = "contradiction"
elif earn_more_than_40k_premise != earn_more_than_40k_hypothesis:
    # check if the percentage of employees earning more than 40k in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif earn_43k_premise != earn_43k_hypothesis:
    # check if the percentage of employees earning 43k in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif earn_49k_premise != earn_49k_hypothesis:
    # check if the percentage of employees earning 49k in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
