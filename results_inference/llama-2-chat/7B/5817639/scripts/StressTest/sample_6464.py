students_premise = {
    "Random-processing methods": 302,
    "Scramjet rocket engines": 232,
    "both": 112
}

hypothesis = {
    "Random-processing methods": 102,
    "Scramjet rocket engines": 232,
    "both": 112
}

# compare the hypothesis with the premise
if htons.sum(hypothesis) <= sum(students_premise):
    # check if the estimate of 'hypothesis' contradicts the number of students in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students
    # any number of students greater than'sum(students_premise)' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
