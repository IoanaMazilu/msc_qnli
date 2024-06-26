math_marks_premise = 76
math_marks_hypothesis = 46
science_marks_premise = 65
science_marks_hypothesis = 65
social_studies_marks_premise = 82
social_studies_marks_hypothesis = 82
english_marks_premise = 67
english_marks_hypothesis = 67
biology_marks_premise = 75
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in various subjects mentioned in the premise
if math_marks_premise <= math_marks_hypothesis:
    # check if the estimate of'math_marks_hypothesis' contradicts the number of math marks in the premise
    label = "contradiction"
elif science_marks_premise!= science_marks_hypothesis or social_studies_marks_premise!= social_studies_marks_hypothesis or english_marks_premise!= english_marks_hypothesis or biology_marks_premise!= biology_marks_hypothesis:
    # check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
