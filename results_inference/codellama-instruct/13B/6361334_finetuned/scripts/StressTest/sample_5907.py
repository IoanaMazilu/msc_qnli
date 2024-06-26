maths_marks_premise = 76
maths_marks_hypothesis = 46
science_marks_premise = 65
science_marks_hypothesis = 65
social_studies_marks_premise = 82
social_studies_marks_hypothesis = 82
english_marks_premise = 67
english_marks_hypothesis = 67
biology_marks_premise = 75
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored in each subject, which are also mentioned in the premise
if maths_marks_hypothesis <= maths_marks_premise:
    # check if the estimate of'maths_marks_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
elif science_marks_hypothesis!= science_marks_premise:
    # check if the number of marks in the hypothesis contradicts the number of marks in the premise
    label = "contradiction"
elif social_studies_marks_hypothesis!= social_studies_marks_premise:
    # check if the number of marks in the hypothesis contradicts the number of marks in the premise
    label = "contradiction"
elif english_marks_hypothesis!= english_marks_premise:
    # check if the number of marks in the hypothesis contradicts the number of marks in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the number of marks in the hypothesis contradicts the number of marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)