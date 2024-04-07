# Premise: In Lulu company 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Hypothesis: In Lulu company less than 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Golden Label: contradiction

earn_less_50k_premise = 60
earn_less_50k_hypothesis = 60

earn_more_40k_premise = 60
earn_more_40k_hypothesis = 60

earn_43k_premise = 11
earn_43k_hypothesis = 11

earn_49k_premise = 5
earn_49k_hypothesis = 5

# the hypothesis refers to the same percentages of salary groups as mentioned in the premise
if earn_less_50k_hypothesis >= earn_less_50k_premise:
    # check if the percentage of employees earning less than 50k in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
elif earn_more_40k_hypothesis != earn_more_40k_premise or earn_43k_hypothesis != earn_43k_premise or earn_49k_hypothesis != earn_49k_premise:
    # check if the percentages of the other salary groups in the hypothesis contradict those mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

