# Premise: If Dan works alone for 12 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Hypothesis: If Dan works alone for less than 42 hours and then stops, how many hours will it take Annie, working alone, to complete the job?
# Golden Label: entailment

dan_hours_worked_premise = 12
dan_hours_worked_hypothesis = 42

# the hypothesis talks about the hours Dan worked, referenced also in the premise
if dan_hours_worked_premise >= dan_hours_worked_hypothesis:
    # check if the premise value contradicts the estimate of less than 'dan_hours_worked_hypothesis'
    label = "contradiction"
elif dan_hours_worked_premise < dan_hours_worked_hypothesis:
    # the hypothesis states a higher maximum for the hours Dan worked
    # the premise value is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"
else:
    # if the premise and hypothesis values are the same, the hypothesis is entailed from the premise
    label = "entailment"

print(label)

