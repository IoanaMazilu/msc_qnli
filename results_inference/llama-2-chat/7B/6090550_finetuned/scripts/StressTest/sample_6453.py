# scores in the premise
score_english = 66
score_mathematics = 60
score_chemistry = 72
score_biology = 77
score_french_language = 55
score_physics = 85

# scores in the hypothesis
score_less_than_76_english = 76
score_less_than_76_mathematics = 60
score_less_than_76_chemistry = 72
score_less_than_76_biology = 77
score_less_than_76_physics = 85

# calculate the average marks in each subject
average_english = score_english / 6
average_mathematics = score_mathematics / 6
average_chemistry = score_chemistry / 6
average_biology = score_biology / 6
average_physics = score_physics / 6

# check if the scores in the hypothesis contradict the scores in the premise
if average_english >= score_less_than_76_english or average_mathematics >= score_less_than_76_mathematics or average_chemistry >= score_less_than_76_chemistry or average_biology >= score_less_than_76_biology or average_physics >= score_less_than_76_physics:
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
