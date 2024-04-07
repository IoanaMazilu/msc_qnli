# Premise: Level-1 college graduates account for 15% of Listco's sales staff.
# Hypothesis: Level-more than 1 college graduates account for 15% of Listco's sales staff.
# Golden Label: contradiction

level_1_graduates_premise = 15
level_1_graduates_hypothesis = 15

# the hypothesis refers to the percentage of Level-more than 1 graduates compared to Level-1 graduates in the premise.
if level_1_graduates_hypothesis != level_1_graduates_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise talks about Level-1 graduates
    # the hypothesis talks about Level-more than 1 graduates
    # these are not the same, hence it's neutral
    label = "neutral"

print(label)

