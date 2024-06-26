geography_marks_premise = 26
geography_marks_hypothesis = 56
history_marks_premise = 60
history_marks_hypothesis = 60
government_marks_premise = 72
government_marks_hypothesis = 72
art_marks_premise = 85
art_marks_hypothesis = 85
computer_science_marks_premise = 80
computer_science_marks_hypothesis = 80

# the hypothesis talks about the marks of a student in different subjects, referenced also in the premise
if geography_marks_hypothesis <= geography_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'geography_marks_premise'
    label = "contradiction"
elif history_marks_hypothesis!= history_marks_premise:
    # check if the history marks in the hypothesis contradict the history marks reported in the premise
    label = "contradiction"
elif government_marks_hypothesis!= government_marks_premise:
    # check if the government marks in the hypothesis contradict the government marks reported in the premise
    label = "contradiction"
elif art_marks_hypothesis!= art_marks_premise:
    # check if the art marks in the hypothesis contradict the art marks reported in the premise
    label = "contradiction"
elif computer_science_marks_hypothesis!= computer_science_marks_premise:
    # check if the computer science marks in the hypothesis contradict the computer science marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks of the student
    # any marks greater than 'geography_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
