english_mark_premise = 76
math_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 76
math_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in various subjects mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the hypothesis value contradicts the premise value for English mark
    label = "contradiction"
elif math_mark_hypothesis >= math_mark_premise:
    # check if the hypothesis value contradicts the premise value for Math mark
    label = "contradiction"
elif physics_mark_hypothesis >= physics_mark_premise:
    # check if the hypothesis value contradicts the premise value for Physics mark
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    # check if the hypothesis value contradicts the premise value for Chemistry mark
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    # check if the hypothesis value contradicts the premise value for Biology mark
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
