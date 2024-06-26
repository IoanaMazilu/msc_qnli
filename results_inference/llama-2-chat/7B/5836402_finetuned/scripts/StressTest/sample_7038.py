# defining variables for the premise
geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
literature_marks_premise = 80

average_marks_premise = geography_marks_premise + history_marks_premise + government_marks_premise + art_marks_premise + literature_marks_premise / 5

# defining variables for the hypothesis
more_than_26_marks_history_premise = 26
more_than_26_marks_geography_premise = 26
more_than_26_marks_government_premise = 26
more_than_26_marks_art_premise = 26
more_than_26_marks_literature_premise = 26

average_marks_hypothesis = geography_marks_premise + history_marks_premise + government_marks_premise + art_marks_premise + literature_marks_premise / 5

# the hypothesis refers to the number of marks obtained in each subject, which are also referenced in the premise
if average_marks_premise <= average_marks_hypothesis:
    # check if the estimate of 'average_marks_hypothesis' contradicts the number of marks obtained in the premise
    label = "contradiction"
elif geography_marks_premise + history_marks_premise + government_marks_premise + art_marks_premise + literature_marks_premise!= average_marks_hypothesis:
    # check if the total number of marks in the hypothesis contradicts the total number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
