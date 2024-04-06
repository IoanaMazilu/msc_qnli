# Premise: Anticipation was also thick in the air in Spain, where hundreds of fans, decked out in red and yellow, arrived early in Madrid's main boulevard to reserve a spot to watch the action on four huge television screens.
# Hypothesis: Thousands also expected to crowd around four big screens in Madrid.
# Golden Label: neutral

fans_premise = 100
fans_hypothesis = 1000
screens_premise = 4
screens_hypothesis = 4

# the hypothesis mentions the number of fans and screens in Madrid, which are also mentioned in the premise
if fans_hypothesis < fans_premise:
    # check if the number of fans in the hypothesis contradicts the number of fans reported in the premise
    label = "contradiction"
elif screens_hypothesis != screens_premise:
    # check if the number of screens from the hypothesis contradicts the number of screens in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)

