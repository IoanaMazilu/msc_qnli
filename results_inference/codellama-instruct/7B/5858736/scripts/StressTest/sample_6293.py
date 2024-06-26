marks_english_premise = 76
marks_mathematics_premise = 65
marks_chemistry_premise = 82
marks_biology_premise = 67
marks_physics_premise = 85

marks_english_hypothesis = 76
marks_mathematics_hypothesis = 65
marks_chemistry_hypothesis = 82
marks_biology_hypothesis = 67
marks_physics_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in all the subjects
if marks_english_hypothesis <= marks_english_premise:
    # check if the estimate of'marks_english_hypothesis' contradicts the marks obtained by Arun in English
    label = "contradiction"
elif marks_mathematics_hypothesis <= marks_mathematics_premise:
    # check if the estimate of'marks_mathematics_hypothesis' contradicts the marks obtained by Arun in Mathematics
    label = "contradiction"
elif marks_chemistry_hypothesis <= marks_chemistry_premise:
    # check if the estimate of'marks_chemistry_hypothesis' contradicts the marks obtained by Arun in Chemistry
    label = "contradiction"
elif marks_biology_hypothesis <= marks_biology_premise:
    # check if the estimate of'marks_biology_hypothesis' contradicts the marks obtained by Arun in Biology
    label = "contradiction"
elif marks_physics_hypothesis <= marks_physics_premise:
    # check if the estimate of'marks_physics_hypothesis' contradicts the marks obtained by Arun in Physics
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
