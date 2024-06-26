english_premise = 86
mathematics_premise = 65
physics_premise = 82
chemistry_premise = 67
biology_premise = 85

english_hypothesis = 76
mathematics_hypothesis = 65
physics_hypothesis = 82
chemistry_hypothesis = 67
biology_hypothesis = 85

# the hypothesis refers to the marks obtained by David in five subjects
if english_hypothesis >= english_premise:
    # check if the English marks in the hypothesis contradict the premise
    label = "contradiction"
elif mathematics_hypothesis > mathematics_premise:
    # check if the Mathematics marks in the hypothesis contradict the premise
    label = "contradiction"
elif physics_hypothesis > physics_premise:
    # check if the Physics marks in the hypothesis contradict the premise
    label = "contradiction"
elif chemistry_hypothesis > chemistry_premise:
    # check if the Chemistry marks in the hypothesis contradict the premise
    label = "contradiction"
elif biology_hypothesis > biology_premise:
    # check if the Biology marks in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise,
    # we can infer entailment as the obtained marks are less than or equal to the marks in the premise
    label = "entailment"

print(label)
