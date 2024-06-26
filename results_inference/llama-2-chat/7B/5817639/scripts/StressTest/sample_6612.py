students_premise = {
    "Random-processing methods": 312,
    "Scramjet rocket engines": 234,
    "both": 112
}

students_hypothesis = {
    "Random-processing methods": 112,
    "Scramjet rocket engines": 234,
    "both": 112
}

# the hypothesis talks about the number of students studying different subjects, referenced also in the premise
if students_hypothesis["Random-processing methods"] <= students_premise["Random-processing methods"] or \
   students_hypothesis["Scramjet rocket engines"] <= students_premise["Scramjet rocket engines"] or \
   students_hypothesis["both"] <= students_premise["both"]:
    # check if the hypothesis value contradicts the estimate of more than'students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying each subject
    # any number of students studying more than'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
