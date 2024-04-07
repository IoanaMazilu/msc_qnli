# Premise: In Arun's company 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Hypothesis: In Arun's company 40% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Golden Label: contradiction

earn_less_50k_premise = 60
earn_more_40k_premise = 60
earn_43k_premise = 11
earn_49k_premise = 5

earn_less_50k_hypothesis = 40
earn_more_40k_hypothesis = 60
earn_43k_hypothesis = 11
earn_49k_hypothesis = 5

# the hypothesis refers to the percentage of employees' earnings mentioned in the premise
if earn_less_50k_hypothesis != earn_less_50k_premise:
    # check if the percentage of employees earning less than $50,000 in the hypothesis contradicts the premise
    label = "contradiction"
elif earn_more_40k_hypothesis != earn_more_40k_premise:
    # check if the percentage of employees earning more than $40,000 in the hypothesis contradicts the premise
    label = "contradiction"
elif earn_43k_hypothesis != earn_43k_premise:
    # check if the percentage of employees earning $43,000 in the hypothesis contradicts the premise
    label = "contradiction"
elif earn_49k_hypothesis != earn_49k_premise:
    # check if the percentage of employees earning $49,000 in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

