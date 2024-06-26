marks_geography = 56
marks_history = 60
marks_government = 72
marks_art = 85
marks_computer_science = 80
marks_modern_literature = 80

# the hypothesis talks about the marks obtained by the student, referenced also in the premise
if marks_geography >= 56 and marks_history >= 60 and marks_government >= 72 and marks_art >= 85 and marks_computer_science >= 80 and marks_modern_literature >= 80:
    # check if the hypothesis value contradicts the estimate of less than'marks_geography'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks obtained by the student
    # any number of marks less than'marks_geography' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
