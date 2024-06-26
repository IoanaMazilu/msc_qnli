marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [46, 65, 82, 67, 85]

# compare the lengths of the lists
if len(marks_hypothesis) <= len(marks_premise):
    # check if the shorter list contradicts the longer list
    label = "contradiction"
else:
    # the lengths of the lists are consistent, but the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
