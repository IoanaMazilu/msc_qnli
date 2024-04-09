math_marks_premise = 76
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 75

math_marks_hypothesis = 76
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in different subjects as mentioned in the premise
if math_marks_hypothesis <= math_marks_premise:
    # check if the estimate of'math_marks_hypothesis' contradicts the number of math marks in the premise
    label = "contradiction"
elif science_marks_hypothesis!= science_marks_premise:
    # check if the number of science marks in the hypothesis contradicts the number of science marks reported in the premise
    label = "contradiction"
elif social_studies_marks_hypothesis!= social_studies_marks_premise:
    # check if the number of social studies marks in the hypothesis contradicts the number of social studies marks reported in the premise
    label = "contradiction"
elif english_marks_hypothesis!= english_marks_premise:
    # check if the number of english marks in the hypothesis contradicts the number of english marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the number of biology marks in the hypothesis contradicts the number of biology marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
