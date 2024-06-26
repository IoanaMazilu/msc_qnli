score_marks_premise = {
    "Mathematics": 76,
    "Science": 65,
    "Social studies": 82,
    "English": 67,
    "Biology": 75
}

score_marks_hypothesis = {
    "Mathematics": None,
    "Science": None,
    "Social studies": None,
    "English": None,
    "Biology": None
}

# the hypothesis talks about the scores in each subject, referenced also in the premise
for subject in score_marks_hypothesis:
    if score_marks_hypothesis[subject] is None:
        # if the score in the hypothesis for the subject is None, it means that the hypothesis cannot be entailed from the premise
        label = "neutral"
    else:
        # if the score in the hypothesis for the subject is not None, it means that the hypothesis can be entailed from the premise
        if score_marks_premise[subject] < score_marks_hypothesis[subject]:
            # check if the score in the hypothesis contradicts the score in the premise
            label = "contradiction"
        else:
            label = "entailment"
    break

print(label)
