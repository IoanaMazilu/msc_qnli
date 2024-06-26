initial_marks_premise = 85
corrected_marks_premise = 50

initial_marks_hypothesis = 85
corrected_marks_hypothesis = 60

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if initial_marks_hypothesis <= initial_marks_premise:
    # check if the hypothesis value contradicts the estimate of 'initial_marks_premise'
    label = "contradiction"
elif corrected_marks_hypothesis!= corrected_marks_premise:
    # check if the corrected marks in the hypothesis contradicts the corrected marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
