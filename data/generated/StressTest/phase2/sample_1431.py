# Premise: How many ways are there for 5 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?
# Hypothesis: How many ways are there for more than 2 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?
# Golden Label: entailment

males_premise = 5
males_hypothesis = 2
females_premise = 3
females_hypothesis = 3

# the hypothesis refers to the number of males and females mentioned in the premise
if males_premise <= males_hypothesis:
    # check if the estimate of 'males_hypothesis' contradicts the number of males in the premise
    label = "contradiction"
elif females_hypothesis != females_premise:
    # check if the number of females in the hypothesis contradicts the number of females reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

