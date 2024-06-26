percent_earn_less_50k_premise = 50
percent_earn_less_50k_hypothesis = 60
percent_earn_more_40k_premise = 60
percent_earn_more_40k_hypothesis = 60
percent_earn_43k_premise = 11
percent_earn_43k_hypothesis = 11
percent_earn_49k_premise = 5
percent_earn_49k_hypothesis = 5

# the hypothesis refers to the percentage of employees earning certain amounts in Richie's company, mentioned in the premise
if percent_earn_less_50k_premise >= percent_earn_less_50k_hypothesis:
    # check if the percentage of employees earning less than 50k in the hypothesis contradicts the premise
    label = "contradiction"
elif percent_earn_more_40k_premise != percent_earn_more_40k_hypothesis:
    # check if the percentage of employees earning more than 40k in the hypothesis contradicts the premise
    label = "contradiction"
elif percent_earn_43k_premise != percent_earn_43k_hypothesis:
    # check if the percentage of employees earning 43k in the hypothesis contradicts the premise
    label = "contradiction"
elif percent_earn_49k_premise != percent_earn_49k_hypothesis:
    # check if the percentage of employees earning 49k in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
