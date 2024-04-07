# Premise: If Dan works alone for 4 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Hypothesis: If Dan works alone for less than 7 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Golden Label: entailment

dan_work_hours_premise = 4
dan_work_hours_hypothesis = 7

# the hypothesis refers to the working hours of Dan mentioned in the premise
if dan_work_hours_hypothesis < dan_work_hours_premise:
    # check if the hypothesized value contradicts the premise
    label = "contradiction"
elif dan_work_hours_hypothesis > dan_work_hours_premise:
    # check if the hypothesized value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

