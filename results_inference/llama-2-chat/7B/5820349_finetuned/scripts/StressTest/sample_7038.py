geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
literature_marks_premise = 80

geography_marks_hypothesis = 26
history_marks_hypothesis = 60
government_marks_hypothesis = 72
art_marks_hypothesis = 85
literature_marks_hypothesis = 80

# the hypothesis refers to the marks obtained in different subjects mentioned in the premise
if geography_marks_premise <= geography_marks_hypothesis:
    # check if the estimate of 'geography_marks_hypothesis' contradicts the marks in Geography in the premise
    label = "contradiction"
elif history_marks_hypothesis!= history_marks_premise or government_marks_hypothesis!= government_marks_premise or art_marks_hypothesis!= art_marks_premise or literature_marks_hypothesis!= literature_marks_premise:
    # check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
