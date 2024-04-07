# Premise: How many ways are there for 2 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?
# Hypothesis: How many ways are there for 6 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?
# Golden Label: contradiction

males_premise = 2
males_hypothesis = 6
females_premise = 3
females_hypothesis = 3

# the hypothesis talks about the number of males and females mentioned in the premise
if males_hypothesis != males_premise or females_hypothesis != females_premise:
    # check if the number of males or females in the hypothesis contradicts the number of males or females in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
