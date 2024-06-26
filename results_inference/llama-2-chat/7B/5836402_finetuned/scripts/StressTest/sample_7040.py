marks_geography_history_government_art_computer_science_modern_literature_premise = [56, 60, 72, 85, 80]
marks_geography_history_government_art_computer_science_modern_literature_hypothesis = [56, 60, 72, 85, 80]

# the hypothesis refers to the marks obtained by a student in specific subjects, which are also mentioned in the premise
if marks_geography_history_government_art_computer_science_modern_literature_hypothesis >= marks_geography_history_government_art_computer_science_modern_literature_premise:
    # check if the estimate of'marks_geography_history_government_art_computer_science_modern_literature_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
