# Premise: If Tina Works independently at the job for more than 5 hours and then Ann works independently, how many hours will it take Ann to complete the remainder of the jobs?
# Hypothesis: If Tina Works independently at the job for 8 hours and then Ann works independently, how many hours will it take Ann to complete the remainder of the jobs?
# Golden Label: neutral

tina_work_hours_premise = 5
tina_work_hours_hypothesis = 8

# the hypothesis talks about the number of hours Tina works, referenced also in the premise
if tina_work_hours_hypothesis <= tina_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'tina_work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Tina works
    # any number of hours greater than 'tina_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

