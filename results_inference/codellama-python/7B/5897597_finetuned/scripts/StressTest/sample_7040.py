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

# the hypothesis refers to the marks obtained in different subjects mentioned in the premise
if geography_marks_hypothesis >= geography_marks_premise:
    # check if the estimate of 'geography_marks_hypothesis' contradicts the marks in geography in the premise
    label = "contradiction"
elif history_marks_hypothesis >= history_marks_premise:
    # check if the estimate of 'history_marks_hypothesis' contradicts the marks in history in the premise
    label = "contradiction"
elif government_marks_hypothesis >= government_marks_premise:
    # check if the estimate of 'government_marks_hypothesis' contradicts the marks in government in the premise
    label = "contradiction"
elif art_marks_hypothesis >= art_marks_premise:
    # check if the estimate of 'art_marks_hypothesis' contradicts the marks in art in the premise
    label = "contradiction"
elif computer_science_marks_hypothesis >= computer_science_marks_premise:
    # check if the estimate of 'computer_science_marks_hypothesis' contradicts the marks in computer science in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
