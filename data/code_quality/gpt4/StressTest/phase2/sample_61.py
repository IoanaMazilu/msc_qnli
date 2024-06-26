less_than_50k_premise = 50
less_than_50k_hypothesis = 60
more_than_40k_premise = 60
more_than_40k_hypothesis = 60
earn_43k_premise = 11
earn_43k_hypothesis = 11
earn_49k_premise = 5
earn_49k_hypothesis = 5

# the hypothesis refers to the percentage of employees earning certain amounts in Arun's company, mentioned in the premise
if less_than_50k_premise >= less_than_50k_hypothesis:
    # check if the estimate of 'less_than_50k_hypothesis' contradicts the percentage of employees earning less than $50,000 in the premise
    label = "contradiction"
elif more_than_40k_premise != more_than_40k_hypothesis:
    # check if the percentage of employees earning more than $40,000 in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif earn_43k_premise != earn_43k_hypothesis:
    # check if the percentage of employees earning $43,000 in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif earn_49k_premise != earn_49k_hypothesis:
    # check if the percentage of employees earning $49,000 in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
