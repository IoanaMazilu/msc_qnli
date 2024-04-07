# Premise: If Dan works alone for less than 7 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Hypothesis: If Dan works alone for 4 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Golden Label: neutral

dan_work_hours_premise = 7
dan_work_hours_hypothesis = 4

# the hypothesis refers to the number of hours Dan works alone, which is also mentioned in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the number of hours Dan works alone in the hypothesis contradicts the premise
    label = "contradiction"
elif dan_work_hours_hypothesis < dan_work_hours_premise:
    # any number of hours less than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

