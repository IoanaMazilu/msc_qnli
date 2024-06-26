english_mark_premise = 76
english_mark_hypothesis = 86
math_mark_premise = 65
math_mark_hypothesis = 65
physics_mark_premise = 82
physics_mark_hypothesis = 82
chemistry_mark_premise = 67
chemistry_mark_hypothesis = 67
biology_mark_premise = 85
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in each subject, as mentioned in the premise
# the hypothesis also specifies the marks for each subject, which are less than the marks in the premise

if english_mark_hypothesis >= english_mark_premise:
    # check if the hypothesis value for English mark contradicts the premise value
    label = "contradiction"
elif math_mark_hypothesis >= math_mark_premise:
    # check if the hypothesis value for Mathematics mark contradicts the premise value
    label = "contradiction"
elif physics_mark_hypothesis >= physics_mark_premise:
    # check if the hypothesis value for Physics mark contradicts the premise value
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    # check if the hypothesis value for Chemistry mark contradicts the premise value
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    # check if the hypothesis value for Biology mark contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
