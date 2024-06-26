english_mark_premise = 72
math_mark_premise = 60
physics_mark_premise = 35
chemistry_mark_premise = 62
biology_mark_premise = 84

english_mark_hypothesis = 22
math_mark_hypothesis = 60
physics_mark_hypothesis = 35
chemistry_mark_hypothesis = 62
biology_mark_hypothesis = 84

# the hypothesis talks about the marks obtained by David, referenced also in the premise
if english_mark_hypothesis > english_mark_premise:
    # check if the english mark in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise:
    # check if the math mark in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif physics_mark_hypothesis != physics_mark_premise:
    # check if the physics mark in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis != chemistry_mark_premise:
    # check if the chemistry mark in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif biology_mark_hypothesis != biology_mark_premise:
    # check if the biology mark in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
else:
    # if all the marks in the hypothesis do not contradict the ones reported in the premise, we can infer entailment
    label = "entailment"

print(label)
