english_marks_premise = 76
english_marks_hypothesis = 46
mathematics_marks_premise = 65
mathematics_marks_hypothesis = 65
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82
biology_marks_premise = 67
biology_marks_hypothesis = 67
physics_marks_premise = 85
physics_marks_hypothesis = 85

# the hypothesis refers to the number of marks obtained in each subject
for subject in ["English", "Mathematics", "Chemistry", "Biology", "Physics"]:
    if getattr(english_marks_hypothesis, subject) > getattr(english_marks_premise, subject):
        # check if the estimate of 'english_marks_hypothesis' contradicts the number of marks obtained in English in the premise
        label = "contradiction"
        break
    elif getattr(mathematics_marks_hypothesis, subject)!= getattr(mathematics_marks_premise, subject):
        # check if the number of marks obtained in Mathematics in the hypothesis contradicts the number of marks obtained in Mathematics in the premise
        label = "contradiction"
        break
    elif getattr(chemistry_marks_hypothesis, subject)!= getattr(chemistry_marks_premise, subject):
        # check if the number of marks obtained in Chemistry in the hypothesis contradicts the number of marks obtained in Chemistry in the premise
        label = "contradiction"
        break
    elif getattr(biology_marks_hypothesis, subject)!= getattr(biology_marks_premise, subject):
        # check if the number of marks obtained in Biology in the hypothesis contradicts the number of marks obtained in Biology in the premise
        label = "contradiction"
        break
    elif getattr(physics_marks_hypothesis, subject)!= getattr(physics_marks_premise, subject):
        # check if the number of marks obtained in Physics in the hypothesis contradicts the number of marks obtained in Physics in the premise
        label = "contradiction"
        break
    else:
        # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"
        break

print(label)
