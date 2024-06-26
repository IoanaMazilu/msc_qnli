marks_premise = [16, 95, 82, 87, 92]
marks_hypothesis = [96, 95, 82, 87, 92]

# the hypothesis talks about the marks obtained by Dacid in specific subjects
for subject in ["English", "Mathematics", "Physics", "Chemistry", "Biology"]:
    # compare the hypothesis value with the premise value for that subject
    if marks_hypothesis[subject] <= marks_premise[subject]:
        # check if the hypothesis value contradicts the estimate of the premise value for that subject
        label = "contradiction"
    else:
        # if the hypothesis value is greater than or equal to the premise value, we can infer entailment
        label = "entailment"
print(label)
