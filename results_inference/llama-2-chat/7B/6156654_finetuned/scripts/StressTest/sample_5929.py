english_marks_premise = 46
mathematics_marks_premise = 85
physics_marks_premise = 92
chemistry_marks_premise = 87
biology_marks_premise = 95

english_marks_hypothesis = 86
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 95

# the hypothesis mentions the marks obtained by Dacid in each subject, which are also mentioned in the premise
if english_marks_hypothesis!= english_marks_premise or mathematics_marks_hypothesis!= mathematics_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
