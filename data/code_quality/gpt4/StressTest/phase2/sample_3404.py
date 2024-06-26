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

# the hypothesis refers to the marks obtained by Dacid in different subjects, which are also mentioned in the premise
if english_mark_hypothesis >= english_mark_premise or math_mark_hypothesis >= math_mark_premise or physics_mark_hypothesis >= physics_mark_premise or chemistry_mark_hypothesis >= chemistry_mark_premise or biology_mark_hypothesis >= biology_mark_premise:
    # check if the hypothesis statement contradicts the premise (hypothesis states less than the marks mentioned in the premise)
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but also does not provide an exact number for the marks, so it cannot be entailed from the premise
    label = "neutral"

print(label)
