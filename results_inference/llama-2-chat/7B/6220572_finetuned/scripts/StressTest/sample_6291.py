marks_english_premise = 76
marks_english_hypothesis = 46
marks_mathematics_premise = 65
marks_mathematics_hypothesis = 65
marks_chemistry_premise = 82
marks_chemistry_hypothesis = 82
marks_biology_premise = 67
marks_biology_hypothesis = 67
marks_physics_premise = 85
marks_physics_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in different subjects, referenced also in the premise
if marks_english_hypothesis <= marks_english_premise:
    # check if the estimate of'marks_english_hypothesis' contradicts the number of marks obtained in English in the premise
    label = "contradiction"
elif marks_mathematics_hypothesis!= marks_mathematics_premise or marks_chemistry_hypothesis!= marks_chemistry_premise or marks_biology_hypothesis!= marks_biology_premise or marks_physics_hypothesis!= marks_physics_premise:
    # check if the marks obtained in the other subjects in the hypothesis contradicts the marks obtained in the same subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
