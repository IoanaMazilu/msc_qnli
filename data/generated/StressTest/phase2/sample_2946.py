# Premise: If Tina Works independently at the job for 8 hours and then Ann works independently, how many hours will it take Ann to complete the remainder of the jobs?
# Hypothesis: If Tina Works independently at the job for more than 5 hours and then Ann works independently, how many hours will it take Ann to complete the remainder of the jobs?
# Golden Label: entailment

tina_work_hours_premise = 8
tina_work_hours_hypothesis = 5

# the hypothesis talks about the number of hours Tina works, referenced also in the premise
if tina_work_hours_premise < tina_work_hours_hypothesis:
    # check if the premise value contradicts the estimate of more than 'tina_work_hours_hypothesis'
    label = "contradiction"
elif tina_work_hours_premise >= tina_work_hours_hypothesis:
    # the premise gives the exact number of hours Tina works
    # any number of hours worked by Tina greater than 'tina_work_hours_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)

