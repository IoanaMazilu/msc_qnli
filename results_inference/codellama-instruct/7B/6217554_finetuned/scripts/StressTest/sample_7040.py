marks_geography_premise = 56
marks_geography_hypothesis = 56
marks_history_premise = 60
marks_history_hypothesis = 60
marks_government_premise = 72
marks_government_hypothesis = 72
marks_art_premise = 85
marks_art_hypothesis = 85
marks_computer_science_premise = 80
marks_computer_science_hypothesis = 80
marks_modern_literature_premise = 80
marks_modern_literature_hypothesis = 80

# the hypothesis refers to the marks obtained by a student in different subjects, referenced also in the premise
if marks_geography_hypothesis >= marks_geography_premise:
    # check if the marks obtained in Geography in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif marks_history_hypothesis >= marks_history_premise:
    # check if the marks obtained in History in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif marks_government_hypothesis >= marks_government_premise:
    # check if the marks obtained in Government in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif marks_art_hypothesis >= marks_art_premise:
    # check if the marks obtained in Art in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif marks_computer_science_hypothesis >= marks_computer_science_premise:
    # check if the marks obtained in Computer Science in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif marks_modern_literature_hypothesis >= marks_modern_literature_premise:
    # check if the marks obtained in Modern Literature in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
