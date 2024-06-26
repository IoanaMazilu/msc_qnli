english_mark_premise = 76
english_mark_hypothesis = 76

mathematics_mark_premise = 65
mathematics_mark_hypothesis = 65

physics_mark_premise = 82
physics_mark_hypothesis = 82

chemistry_mark_premise = 67
chemistry_mark_hypothesis = 67

biology_mark_premise = 85
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in each subject, as mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the hypothesis value contradicts the premise value for English marks
    label = "contradiction"
elif mathematics_mark_hypothesis >= mathematics_mark_premise:
    # check if the hypothesis value contradicts the premise value for Mathematics marks
    label = "contradiction"
elif physics_mark_hypothesis >= physics_mark_premise:
    # check if the hypothesis value contradicts the premise value for Physics marks
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    # check if the hypothesis value contradicts the premise value for Chemistry marks
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    # check if the hypothesis value contradicts the premise value for Biology marks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
