# Premise: Following the approval of crude oil production cuts by OPEC, the price of crude which has slumped by 28% in the last 3 months is expected to rally and increase by about 5% in the next one month.
# Hypothesis: Following the approval of crude oil production cuts by OPEC, the price of crude which has slumped by more than 28% in the last 3 months is expected to rally and increase by about 5% in the next one month.
# Golden Label: contradiction

crude_slump_premise = 28
crude_slump_hypothesis = 28

# the hypothesis refers to the slump in crude oil prices mentioned in the premise
if crude_slump_hypothesis > crude_slump_premise:
    # check if the slump in crude oil prices in the hypothesis contradicts the slump in crude oil prices reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

