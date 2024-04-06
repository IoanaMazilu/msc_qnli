# Premise: Employers Cut Payrolls for Sixth Straight Month, 62,000 Drop In May.
# Hypothesis: Employers Cut Workers for a Sixth Month-June's total: 62,000.
# Golden Label: neutral

month_count_premise = 6
month_count_hypothesis = 6
drop_count_premise = 62000
drop_count_hypothesis = 62000

# the hypothesis and premise mention the number of months employers have been cutting payrolls and the total number of workers cut
if month_count_premise != month_count_hypothesis:
    # check if the number of months in the hypothesis contradicts the number of months in the premise
    label = "contradiction"
elif drop_count_premise != drop_count_hypothesis:
    # check if the number of workers cut in the hypothesis contradicts the number of workers cut in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

