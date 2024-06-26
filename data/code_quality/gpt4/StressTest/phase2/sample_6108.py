level_1_graduates_premise = 15
level_4_graduates_hypothesis = 15

# the hypothesis talks about the percentage of level-4 graduates in the sales staff, while the premise talks about level-1 graduates
if level_4_graduates_hypothesis < level_1_graduates_premise:
    # check if the hypothesis value contradicts the percentage of level-1 graduates in the premise
    label = "contradiction"
elif level_4_graduates_hypothesis > level_1_graduates_premise:
    # check if the hypothesis value contradicts the percentage of level-1 graduates in the premise
    label = "contradiction"
else:
    # the premise gives the percentage of level-1 graduates
    # the hypothesis refers to level-4 graduates which cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
