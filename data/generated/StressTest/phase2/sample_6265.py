# Premise: If Dan works alone for more than 2 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Hypothesis: If Dan works alone for 3 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Golden Label: neutral

dan_work_hours_premise = 2
dan_work_hours_hypothesis = 3

# The hypothesis refers to the number of hours Dan works alone, which is also mentioned in the premise
if dan_work_hours_hypothesis <= dan_work_hours_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'dan_work_hours_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of hours Dan works
    # Any number of hours greater than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

