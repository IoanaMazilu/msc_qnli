# Premise: If Dan works alone for 8 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Hypothesis: If Dan works alone for more than 8 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Golden Label: contradiction

dan_work_hours_premise = 8
dan_work_hours_hypothesis = 8

# the hypothesis refers to the number of hours Dan works alone, which is also mentioned in the premise
if dan_work_hours_hypothesis != dan_work_hours_premise:
    # check if the number of hours Dan works in the hypothesis contradicts the number of hours Dan works in the premise
    label = "contradiction"
else:
    # if the number of hours Dan works in the hypothesis does not contradict the number of hours Dan works in the premise, we can infer entailment
    label = "entailment"

print(label)

