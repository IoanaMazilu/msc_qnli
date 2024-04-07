# Premise: If Dan works alone for less than 42 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Hypothesis: If Dan works alone for 12 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Golden Label: neutral

dan_hours_worked_premise = 42
dan_hours_worked_hypothesis = 12

# the hypothesis refers to the number of hours Dan works, which is also mentioned in the premise
if dan_hours_worked_hypothesis >= dan_hours_worked_premise:
    # check if the number of hours in the hypothesis contradicts the premise value of less than 'dan_hours_worked_premise'
    label = "contradiction"
elif dan_hours_worked_hypothesis > dan_hours_worked_premise:
    # check if the number of hours Dan works in the hypothesis is more than the hours mentioned in the premise
    label = "contradiction"
else:
    # any number of hours less than 'dan_hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
   
print(label)

