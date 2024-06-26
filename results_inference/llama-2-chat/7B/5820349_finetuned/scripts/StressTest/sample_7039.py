geography_history_government_mark_premise = 26
geography_history_government_mark_hypothesis = 56
art_mark_premise = 60
art_mark_hypothesis = 60
computer_science_mark_premise = 72
computer_science_mark_hypothesis = 72
modern_literature_mark_premise = 85
modern_literature_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by a student in different subjects mentioned in the premise
if geography_history_government_mark_hypothesis <= geography_history_government_mark_premise:
    # check if the mark in Geography, History and Government in the hypothesis contradicts the estimate of more than 'geography_history_government_mark_premise'
    label = "contradiction"
elif art_mark_hypothesis!= art_mark_premise:
    # check if the mark in Art in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif computer_science_mark_hypothesis!= computer_science_mark_premise:
    # check if the mark in Computer Science in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif modern_literature_mark_hypothesis!= modern_literature_mark_premise:
    # check if the mark in Modern Literature in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the mark in Geography, History and Government
    # any mark greater than 'geography_history_government_mark_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
