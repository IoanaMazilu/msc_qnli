english_marks_premise = 20
english_marks_hypothesis = 90
mathematics_marks_premise = 92
mathematics_marks_hypothesis = 92
physics_marks_premise = 85
physics_marks_hypothesis = 85
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 85
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in different subjects, as mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the marks in english in the hypothesis contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif mathematics_marks_hypothesis != mathematics_marks_premise or physics_marks_hypothesis != physics_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if the marks in any other subject in the hypothesis contradicts the exact marks mentioned in the premise
    label = "contradiction"
else:
    # the premise indicates Dacid scored more than 20 in English, and the exact marks in other subjects. 
    # So, the hypothesis is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)
