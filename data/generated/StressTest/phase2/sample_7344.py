# Premise: Following the approval of crude oil production cuts by OPEC, the price of crude which has slumped by 28% in the last 3 months is expected to rally and increase by about 5% in the next one month.
# Hypothesis: Following the approval of crude oil production cuts by OPEC, the price of crude which has slumped by less than 68% in the last 3 months is expected to rally and increase by about 5% in the next one month.
# Golden Label: entailment

crude_slump_premise = 28
crude_slump_hypothesis = 68

# the hypothesis refers to the percentage slump of crude price mentioned in the premise
if crude_slump_premise >= crude_slump_hypothesis:
    # check if the estimate of 'crude_slump_hypothesis' contradicts the percentage slump in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

