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

# the hypothesis talks about the average marks of a student who obtained more than 26 marks in each subject
if geography_marks_hypothesis <= geography_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'geography_marks_premise'
    label = "contradiction"
elif history_marks_hypothesis <= history_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'history_marks_premise'
    label = "contradiction"
elif government_marks_hypothesis <= government_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'government_marks_premise'
    label = "contradiction"
elif art_marks_hypothesis <= art_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'art_marks_premise'
    label = "contradiction"
elif literature_marks_hypothesis <= literature_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'literature_marks_premise'
    label = "contradiction"
else:
    # the premise gives the average marks of a student who obtained more than 26 marks in each subject
    # any number of marks greater than 'geography_marks_premise', 'history_marks_premise', 'government_marks_premise', 'art_marks_premise' and 'literature_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
