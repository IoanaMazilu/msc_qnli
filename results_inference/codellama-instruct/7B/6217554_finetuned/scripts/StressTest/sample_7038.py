# define variables for the marks obtained by the student in each subject
geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
computer_science_marks_premise = 80
modern_literature_marks_premise = 80

# define the hypothesis variables
geography_marks_hypothesis = 26
history_marks_hypothesis = 60
government_marks_hypothesis = 72
art_marks_hypothesis = 85
computer_science_marks_hypothesis = 80
modern_literature_marks_hypothesis = 80

# check if the hypothesis values contradict the premise ones
if geography_marks_hypothesis >= geography_marks_premise:
    label = "contradiction"
elif history_marks_hypothesis!= history_marks_premise:
    label = "contradiction"
elif government_marks_hypothesis!= government_marks_premise:
    label = "contradiction"
elif art_marks_hypothesis!= art_marks_premise:
    label = "contradiction"
elif computer_science_marks_hypothesis!= computer_science_marks_premise:
    label = "contradiction"
elif modern_literature_marks_hypothesis!= modern_literature_marks_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
