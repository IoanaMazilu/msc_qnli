# define variables for the scores in each subject
score_english = 66
score_mathematics = 60
score_chemistry = 72
score_biology = 77
score_french_language = 55
score_physics = 85

# the hypothesis refers to the scores in each subject mentioned in the premise
if score_english >= score_english:
    # check if the hypothesis estimate contradicts the score in English in the premise
    label = "contradiction"
elif score_mathematics >= score_mathematics:
    # check if the hypothesis estimate contradicts the score in Mathematics in the premise
    label = "contradiction"
elif score_chemistry >= score_chemistry:
    # check if the hypothesis estimate contradicts the score in Chemistry in the premise
    label = "contradiction"
elif score_biology >= score_biology:
    # check if the hypothesis estimate contradicts the score in Biology in the premise
    label = "contradiction"
elif score_french_language >= score_french_language:
    # check if the hypothesis estimate contradicts the score in French Language in the premise
    label = "contradiction"
elif score_physics >= score_physics:
    # check if the hypothesis estimate contradicts the score in Physics in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
