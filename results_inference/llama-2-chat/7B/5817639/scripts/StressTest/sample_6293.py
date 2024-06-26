marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [65, 76, 82, 67, 85]

# the hypothesis refers to the marks obtained by Arun in the subjects mentioned in the premise
if any(marks_hypothesis <= marks_premise):
    # check if the hypothesis value contradicts any of the marks in the premise
    label = "contradiction"
else:
    # the premise provides a range of marks obtained by Arun in each subject
    # any marks within the range is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
