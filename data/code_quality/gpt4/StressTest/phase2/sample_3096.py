earn_less_premise = 60
earn_less_hypothesis = 50
earn_more_premise = 60
earn_more_hypothesis = 60
earn_43_premise = 11
earn_43_hypothesis = 11
earn_49_premise = 5
earn_49_hypothesis = 5

# the hypothesis refers to the percentage of employees' earnings mentioned in the premise
if earn_less_premise < earn_less_hypothesis:
    # check if the estimate of 'earn_less_hypothesis' contradicts the percentage of employees earning less than $50,000 in the premise
    label = "contradiction"
elif earn_more_hypothesis != earn_more_premise:
    # check if the percentage of employees earning more than $40,000 in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif earn_43_hypothesis != earn_43_premise:
    # check if the percentage of employees earning $43,000 in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif earn_49_hypothesis != earn_49_premise:
    # check if the percentage of employees earning $49,000 in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
