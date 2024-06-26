marks_english_premise = 96
marks_mathematics_premise = 95
marks_physics_premise = 82
marks_chemistry_premise = 87
marks_biology_premise = 92

marks_english_hypothesis = 96
marks_mathematics_hypothesis = 95
marks_physics_hypothesis = 82
marks_chemistry_hypothesis = 87
marks_biology_hypothesis = 92

# the hypothesis talks about the marks obtained by Dacid in each subject, referenced also in the premise
if marks_english_hypothesis >= marks_english_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_english_premise'
    label = "contradiction"
elif marks_mathematics_hypothesis >= marks_mathematics_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_mathematics_premise'
    label = "contradiction"
elif marks_physics_hypothesis >= marks_physics_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_physics_premise'
    label = "contradiction"
elif marks_chemistry_hypothesis >= marks_chemistry_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_chemistry_premise'
    label = "contradiction"
elif marks_biology_hypothesis >= marks_biology_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_biology_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
