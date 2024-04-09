english_marks_premise = 76
english_marks_hypothesis = 65
mathematics_marks_premise = 65
mathematics_marks_hypothesis = 82
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 67
biology_marks_premise = 67
biology_marks_hypothesis = 85
physics_marks_premise = 85
physics_marks_hypothesis = 76

# the hypothesis refers to the marks obtained in each subject
for subject in ["English", "Mathematics", "Chemistry", "Biology", "Physics"]:
    # check if the hypothesis value contradicts the premise value for that subject
    if hypothesis_value =< premise_value:
        label = "contradiction"
        break
    elif hypothesis_value!= premise_value:
        label = "neutral"
        break
    else:
        # if the hypothesis value is consistent with the premise value, we can infer entailment
        label = "entailment"

print(label)
