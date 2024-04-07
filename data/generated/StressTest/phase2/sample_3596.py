# Premise: In Winchard's company 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Hypothesis: In Winchard's company 30% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Golden Label: contradiction

earn_less_50k_premise = 60
earn_less_50k_hypothesis = 30
earn_more_40k_premise = 60
earn_more_40k_hypothesis = 60
earn_43k_premise = 11
earn_43k_hypothesis = 11
earn_49k_premise = 5
earn_49k_hypothesis = 5

# the hypothesis refers to the percentage of employees that earn different amounts of money, the same as the premise
if earn_less_50k_premise != earn_less_50k_hypothesis:
    # check if the percentage of employees that earn less than 50k in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif earn_more_40k_premise != earn_more_40k_hypothesis:
    # check if the percentage of employees that earn more than 40k in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif earn_43k_premise != earn_43k_hypothesis:
    # check if the percentage of employees that earn 43k in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif earn_49k_premise != earn_49k_hypothesis:
    # check if the percentage of employees that earn 49k in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

