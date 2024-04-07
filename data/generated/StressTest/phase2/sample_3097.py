# Premise: In Richie's company more than 50% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Hypothesis: In Richie's company 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Golden Label: neutral

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

