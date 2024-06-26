math_marks_premise = 46
math_marks_hypothesis = 76
science_marks_premise = 65
science_marks_hypothesis = 65
social_studies_marks_premise = 82
social_studies_marks_hypothesis = 82
english_marks_premise = 67
english_marks_hypothesis = 67
biology_marks_premise = 75
biology_marks_hypothesis = 75

# the hypothesis talks about the marks scored by Shekar in different subjects, referenced also in the premise
if math_marks_hypothesis <= math_marks_premise or science_marks_hypothesis!= science_marks_premise or social_studies_marks_hypothesis!= social_studies_marks_premise or english_marks_hypothesis!= english_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than'math_marks_premise' or if the marks in any other subject are different from the premise
    label = "contradiction"
elif math_marks_hypothesis > math_marks_premise and science_marks_hypothesis == science_marks_premise and social_studies_marks_hypothesis == social_studies_marks_premise and english_marks_hypothesis == english_marks_premise and biology_marks_hypothesis == biology_marks_premise:
    # check if the hypothesis value is greater than'math_marks_premise' and the marks in all other subjects are same as the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
