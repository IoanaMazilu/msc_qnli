# Premise: Reena and Shaloo are partners in a business, Reena invests Rs, 35,000 for 8 months and Shaloo invests Rs.
# Hypothesis: Reena and Shaloo are partners in a business, Reena invests Rs, 35,000 for more than 4 months and Shaloo invests Rs.
# Golden Label: entailment

investment_duration_Reena_premise = 8
investment_duration_Reena_hypothesis = 4

# the hypothesis refers to the duration of Reena's investment mentioned in the premise
if investment_duration_Reena_premise <= investment_duration_Reena_hypothesis:
    # check if the estimate of 'investment_duration_Reena_hypothesis' contradicts the duration of Reena's investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

