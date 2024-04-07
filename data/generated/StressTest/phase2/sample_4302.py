# Premise: In Parkin's company 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Hypothesis: In Parkin's company more than 20% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Golden Label: entailment

earn_less_50k_premise = 60
earn_less_50k_hypothesis = 20
earn_more_40k_premise = 60
earn_more_40k_hypothesis = 60
earn_43k_premise = 11
earn_43k_hypothesis = 11
earn_49k_premise = 5
earn_49k_hypothesis = 5

# the hypothesis suggests the percentage of employees earning less than $50,000 a year, more than $40,000 a year, 
# exactly $43,000 a year and exactly $49,000 a year in Parkin's company, all mentioned in the premise
if earn_less_50k_premise < earn_less_50k_hypothesis:
    # check if the estimate of 'earn_less_50k_hypothesis' contradicts the percentage of employees earning less than $50,000 a year in the premise
    label = "contradiction"
elif earn_more_40k_hypothesis != earn_more_40k_premise:
    # check if the percentage of employees earning more than $40,000 a year in the hypothesis contradicts the same percentage reported in the premise
    label = "contradiction"
elif earn_43k_hypothesis != earn_43k_premise:
    # check if the percentage of employees earning exactly $43,000 a year in the hypothesis contradicts the same percentage reported in the premise
    label = "contradiction"
elif earn_49k_hypothesis != earn_49k_premise:
    # check if the percentage of employees earning exactly $49,000 a year in the hypothesis contradicts the same percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

