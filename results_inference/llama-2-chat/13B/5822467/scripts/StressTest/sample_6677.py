english_marks_premise = 96
english_marks_hypothesis = 95
mathematics_marks_premise = 95
mathematics_marks_hypothesis = 92
physics_marks_premise = 82
physics_marks_hypothesis = 87
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 92
biology_marks_premise = 92
biology_marks_hypothesis = 87

# the hypothesis refers to the marks obtained in each subject
for subject in ["English", "Mathematics", "Physics", "Chemistry", "Biology"]:
    if hypothesis_marks = <hypothesis_marks[subject]):
        # check if the hypothesis mark is less than the premise mark
        if premise_marks = <premise_marks[subject]>:
            if hypothesis_marks <= premise_marks:
                # if the hypothesis mark is less than or equal to the premise mark, we have contradiction
                label = "contradiction"
                break
            else:
                # if the hypothesis mark is greater than the premise mark, we have entailment
                label = "entailment"
                break
        else:
            # if the premise mark is not available, we cannot infer entailment or contradiction
            label = "neutral"
            break
    else:
        # if the hypothesis mark is not available, we cannot infer entailment or contradiction
        label = "neutral"
        break

print(label)
