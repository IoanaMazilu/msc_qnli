marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [66, 65, 82, 67, 85]

# the hypothesis talks about the marks obtained by Arun in 6 subjects
if any(marks_hypothesis <= marks_premise):
    # check if the hypothesis value contradicts the estimate of marks obtained by Arun in any of the subjects
    label = "contradiction"
else:
    # the premise gives an estimate for the marks obtained by Arun in all subjects
    # any marks value greater than the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
