# Premise: In Arun's company 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Hypothesis: In Arun's company more than 50% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Golden Label: entailment

earn_less_premise = 60
earn_less_hypothesis = 50
earn_more_premise = 60
earn_more_hypothesis = 60
earn_43k_premise = 11
earn_43k_hypothesis = 11
earn_49k_premise = 5
earn_49k_hypothesis = 5

# the hypothesis refers to the percentages of earnings mentioned in the premise
if earn_less_premise != earn_less_hypothesis:
    # check if the estimate of 'earn_less_hypothesis' contradicts the percentage of 'earn_less_premise'
    label = "contradiction"
elif earn_more_hypothesis != earn_more_premise:
    # check if the estimate of 'earn_more_hypothesis' contradicts the percentage of 'earn_more_premise'
    label = "contradiction"
elif earn_43k_hypothesis != earn_43k_premise:
    # check if the estimate of 'earn_43k_hypothesis' contradicts the percentage of 'earn_43k_premise'
    label = "contradiction"
elif earn_49k_hypothesis != earn_49k_premise:
    # check if the estimate of 'earn_49k_hypothesis' contradicts the percentage of 'earn_49k_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

