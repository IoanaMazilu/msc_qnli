english_mark_premise = 85  # upper limit of the score
english_mark_hypothesis = 65
physics_mark = 78
math_mark = 89
chemistry_mark = 51
biology_mark = 69

# the hypothesis refers to the same exam scores mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the English mark in the hypothesis contradicts the upper limit given in the premise
    label = "contradiction"
else:
    # if the English mark does not contradict the premise, it is possible for Nancy to have scored this mark
    # hence, the hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
