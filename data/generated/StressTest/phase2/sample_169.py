# Premise: In Lulu company more than 20% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Hypothesis: In Lulu company 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Golden Label: neutral

less_than_50k_premise = 20
less_than_50k_hypothesis = 60
more_than_40k_premise = 60
more_than_40k_hypothesis = 60
earn_43k_premise = 11
earn_43k_hypothesis = 11
earn_49k_premise = 5
earn_49k_hypothesis = 5

# the hypothesis refers to the same percentages of salary ranges mentioned in the premise
if less_than_50k_hypothesis <= less_than_50k_premise:
    # check if the percentage of 'less_than_50k_hypothesis' contradicts the estimate in the premise
    label = "contradiction"
elif more_than_40k_hypothesis != more_than_40k_premise:
    # check if the percentage of 'more_than_40k_hypothesis' contradicts the percentage in the premise
    label = "contradiction"
elif earn_43k_hypothesis != earn_43k_premise:
    # check if the percentage of 'earn_43k_hypothesis' contradicts the percentage in the premise
    label = "contradiction"
elif earn_49k_hypothesis != earn_49k_premise:
    # check if the percentage of 'earn_49k_hypothesis' contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we cannot infer entailment
    label = "neutral"

print(label)

