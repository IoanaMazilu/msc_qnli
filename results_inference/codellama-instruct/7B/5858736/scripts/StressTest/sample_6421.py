marks_english_premise = 66
marks_mathematics_premise = 65
marks_chemistry_premise = 82
marks_biology_premise = 67
marks_physics_premise = 85
marks_total_premise = 66 + 65 + 82 + 67 + 85

marks_english_hypothesis = 76
marks_mathematics_hypothesis = 65
marks_chemistry_hypothesis = 82
marks_biology_hypothesis = 67
marks_physics_hypothesis = 85
marks_total_hypothesis = 76 + 65 + 82 + 67 + 85

# the hypothesis talks about the marks obtained by Arun in each subject, referenced also in the premise
if marks_english_hypothesis <= marks_english_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_english_premise'
    label = "contradiction"
elif marks_mathematics_hypothesis <= marks_mathematics_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_mathematics_premise'
    label = "contradiction"
elif marks_chemistry_hypothesis <= marks_chemistry_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_chemistry_premise'
    label = "contradiction"
elif marks_biology_hypothesis <= marks_biology_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_biology_premise'
    label = "contradiction"
elif marks_physics_hypothesis <= marks_physics_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_physics_premise'
    label = "contradiction"
elif marks_total_hypothesis <= marks_total_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_total_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
