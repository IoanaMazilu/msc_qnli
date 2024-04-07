# Premise: Level-1 college graduates account for 15% of Amtek's sales staff.
# Hypothesis: Level-more than 1 college graduates account for 15% of Amtek's sales staff.
# Golden Label: contradiction

level1_graduates_premise = 15
level_more_than_1_graduates_hypothesis = 15

# the hypothesis talks about the percentage of level-1 and more graduates in a company's sales staff, referenced also in the premise
if level_more_than_1_graduates_hypothesis != level1_graduates_premise:
    # check if the percentage of level-more-than-1 graduates in the hypothesis contradicts the percentage of level-1 graduates in the premise
    label = "contradiction"
else:
    # the premise provides precise data for the percentage of level-1 graduates
    # the same percentage for level-more-than-1 graduates cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

