english_marks_premise = 86
english_marks_hypothesis = 85
mathematics_marks_premise = 85
mathematics_marks_hypothesis = 82
physics_marks_premise = 82
physics_marks_hypothesis = 87
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 85
biology_marks_premise = 85
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained in each subject
for subject in ["English", "Mathematics", "Physics", "Chemistry", "Biology"]:
    # check if the hypothesis value contradicts the premise value
    if getattr(subject, "marks_premise") <= getattr(subject, "marks_hypothesis"):
        label = "contradiction"
        break
    elif getattr(subject, "marks_hypothesis")!= getattr(subject, "marks_premise"):
        label = "contradiction"
        break
    else:
        # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"
        break
else:
    # if no contradiction was found, the hypothesis is neutral with respect to the premise
    label = "neutral"

print(label)
