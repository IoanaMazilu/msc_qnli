english_premise = 56
mathematics_premise = 65
chemistry_premise = 82
biology_premise = 67
physics_premise = 85

english_hypothesis = 76
mathematics_hypothesis = 65
chemistry_hypothesis = 82
biology_hypothesis = 67
physics_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in English, Mathematics, Chemistry, Biology and Physics
if english_hypothesis <= english_premise:
    # check if the English marks in the hypothesis contradict the premise
    label = "contradiction"
elif mathematics_hypothesis != mathematics_premise:
    # check if the Mathematics marks in the hypothesis contradict the premise
    label = "contradiction"
elif chemistry_hypothesis != chemistry_premise:
    # check if the Chemistry marks in the hypothesis contradict the premise
    label = "contradiction"
elif biology_hypothesis != biology_premise:
    # check if the Biology marks in the hypothesis contradict the premise
    label = "contradiction"
elif physics_hypothesis != physics_premise:
    # check if the Physics marks in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
