earn_less_50k_premise = 60
earn_less_50k_hypothesis = 10
earn_more_40k_premise = 60
earn_more_40k_hypothesis = 60
earn_43k_premise = 11
earn_43k_hypothesis = 11
earn_49k_premise = 5
earn_49k_hypothesis = 5

# the hypothesis refers to the same categories of employees' earnings in Parkin's company as the premise
if earn_less_50k_premise != earn_less_50k_hypothesis:
    # check if the percentage of employees earning less than $50,000 contradicts the one in the premise
    label = "contradiction"
elif earn_more_40k_premise != earn_more_40k_hypothesis:
    # check if the percentage of employees earning more than $40,000 contradicts the one in the premise
    label = "contradiction"
elif earn_43k_premise != earn_43k_hypothesis:
    # check if the percentage of employees earning exactly $43,000 contradicts the one in the premise
    label = "contradiction"
elif earn_49k_premise != earn_49k_hypothesis:
    # check if the percentage of employees earning exactly $49,000 contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values match exactly the premise ones, we can infer entailment
    label = "entailment"

print(label)
