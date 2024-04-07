# Premise: How many ways are there for more than 2 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?
# Hypothesis: How many ways are there for 5 males and 3 females to sit (around a circular table) if no male should sit next to a male (and no female next to female) and Mary wants to sit with her back on the wall?
# Golden Label: neutral

males_premise = 2
males_hypothesis = 5
females_premise = 3
females_hypothesis = 3

# the hypothesis refers to the number of males and females sitting around a table, which is also mentioned in the premise
if males_hypothesis <= males_premise:
    # check if the number of males in the hypothesis contradicts the premise estimate of more than 'males_premise' males
    label = "contradiction"
elif females_hypothesis != females_premise:
    # check if the number of females in the hypothesis contradicts the number of females reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males
    # any number of males greater than 'males_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

