# Premise: How many ways are there for 5 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?
# Hypothesis: How many ways are there for 8 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?
# Golden Label: contradiction

males_premise = 5
females_premise = 3
males_hypothesis = 8
females_hypothesis = 3

# the hypothesis refers to the number of males and females from the premise
if males_premise != males_hypothesis:
    # check if the number of males in the hypothesis contradicts the number of males reported in the premise
    label = "contradiction"
elif females_premise != females_hypothesis:
    # check if the number of females in the hypothesis contradicts the number of females reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
