english_marks_premise = 16
mathematics_marks_premise = 89
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 81

english_marks_hypothesis = 86
mathematics_marks_hypothesis = 89
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 81

# the hypothesis talks about the marks obtained by Dacid in different subjects
# we can't compare the marks directly as the premise does not mention the marks obtained by Dacid in the same subjects
# the hypothesis does not contradict the premise, but it cannot be entailed from the premise either
label = "neutral"

print(label)
