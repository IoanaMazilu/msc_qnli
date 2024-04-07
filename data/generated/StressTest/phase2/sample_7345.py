# Premise: Following the approval of crude oil production cuts by OPEC, the price of crude which has slumped by less than 68% in the last 3 months is expected to rally and increase by about 5% in the next one month.
# Hypothesis: Following the approval of crude oil production cuts by OPEC, the price of crude which has slumped by 28% in the last 3 months is expected to rally and increase by about 5% in the next one month.
# Golden Label: neutral

slump_premise = 68
slump_hypothesis = 28
increase_premise = 5
increase_hypothesis = 5

# the hypothesis refers to the percentage of slump and increase in crude oil prices mentioned in the premise
if slump_premise != slump_hypothesis:
    # check if the slump percentage in the hypothesis contradicts the slump percentage in the premise
    label = "contradiction"
elif increase_premise != increase_hypothesis:
    # check if the increase percentage in the hypothesis contradicts the increase percentage in the premise
    label = "contradiction"
else:
    # if the slump and increase percentages in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

