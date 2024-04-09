english_marks_premise = 96
mathematics_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 92

english_marks_hypothesis = 96
mathematics_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 92

# the hypothesis refers to the marks obtained by Dacid in various subjects mentioned in the premise
if english_marks_hypothesis >= english_marks_premise:
    # check if the estimate of 'english_marks_hypothesis' contradicts the mark in English in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
