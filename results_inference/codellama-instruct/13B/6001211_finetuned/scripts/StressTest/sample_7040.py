geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
computer_science_marks_premise = 80

geography_marks_hypothesis = 56
history_marks_hypothesis = 60
government_marks_hypothesis = 72
art_marks_hypothesis = 85
computer_science_marks_hypothesis = 80

# the hypothesis refers to the marks obtained by a student in various subjects, mentioned also in the premise
if geography_marks_hypothesis >= geography_marks_premise:
    # check if the hypothesis value contradicts the estimate of 'geography_marks_premise'
    label = "contradiction"
elif history_marks_hypothesis >= history_marks_premise:
    # check if the hypothesis value contradicts the estimate of 'history_marks_premise'
    label = "contradiction"
elif government_marks_hypothesis >= government_marks_premise:
    # check if the hypothesis value contradicts the estimate of 'government_marks_premise'
    label = "contradiction"
elif art_marks_hypothesis >= art_marks_premise:
    # check if the hypothesis value contradicts the estimate of 'art_marks_premise'
    label = "contradiction"
elif computer_science_marks_hypothesis >= computer_science_marks_premise:
    # check if the hypothesis value contradicts the estimate of 'computer_science_marks_premise'
    label = "contradiction"
else:
    # the premise gives exact marks for each subject
    # any marks less than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
