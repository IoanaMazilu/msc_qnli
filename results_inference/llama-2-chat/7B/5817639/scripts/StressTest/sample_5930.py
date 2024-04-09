marks_premise = [86, 85, 92, 87, 95]
marks_hypothesis = [less_than_86, less_than_85, less_than_92, less_than_87, less_than_95]

# the hypothesis refers to the marks obtained by Dacid in each subject, as mentioned in the premise
for subject in marks_premise:
    if marks_hypothesis[subject] <= marks_premise[subject]:
        # check if the hypothesis value contradicts the estimate of marks in the premise
        label = "contradiction"
    else:
        # the premise gives only an estimate for the marks in each subject
        # any marks less than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"
print(label)
