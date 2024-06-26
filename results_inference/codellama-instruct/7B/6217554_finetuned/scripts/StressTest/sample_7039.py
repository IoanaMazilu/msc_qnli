# define variables for the marks obtained by the student in each subject
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
modern_literature_marks_premise = 80
modern_literature_marks_hypothesis = 80

# the hypothesis talks about the marks obtained by the student in each subject, referenced also in the premise
if geography_marks_hypothesis <= geography_marks_premise:
    # check if the marks obtained in Geography in the hypothesis contradict the estimate of more than 'geography_marks_premise'
    label = "contradiction"
elif history_marks_hypothesis!= history_marks_premise:
    # check if the marks obtained in History in the hypothesis contradict the marks obtained in History in the premise
    label = "contradiction"
elif government_marks_hypothesis!= government_marks_premise:
    # check if the marks obtained in Government in the hypothesis contradict the marks obtained in Government in the premise
    label = "contradiction"
elif art_marks_hypothesis!= art_marks_premise:
    # check if the marks obtained in Art in the hypothesis contradict the marks obtained in Art in the premise
    label = "contradiction"
elif computer_science_marks_hypothesis!= computer_science_marks_premise:
    # check if the marks obtained in Computer Science in the hypothesis contradict the marks obtained in Computer Science in the premise
    label = "contradiction"
elif modern_literature_marks_hypothesis!= modern_literature_marks_premise:
    # check if the marks obtained in Modern Literature in the hypothesis contradict the marks obtained in Modern Literature in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
