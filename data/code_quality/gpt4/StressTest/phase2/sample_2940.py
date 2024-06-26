work_hours_tina_premise = 12
work_hours_tina_hypothesis = 82

# the hypothesis refers to the time Tina takes to complete a job, which is also mentioned in the premise
if work_hours_tina_hypothesis < work_hours_tina_premise:
    # if 'work_hours_tina_hypothesis' is less than 'work_hours_tina_premise', this contradicts the premise
    label = "contradiction"
elif work_hours_tina_hypothesis == work_hours_tina_premise:
    # if 'work_hours_tina_hypothesis' is equal to 'work_hours_tina_premise', this can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # if 'work_hours_tina_hypothesis' is more than 'work_hours_tina_premise', this does not contradict the premise but cannot be fully and explicitly entailed from it
    label = "neutral"

print(label)
