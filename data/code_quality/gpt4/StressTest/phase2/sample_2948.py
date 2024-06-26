tina_work_hours_premise = 8
tina_work_hours_hypothesis = 7

# the hypothesis talks about the working hours of Tina, which is also mentioned in the premise
if tina_work_hours_hypothesis != tina_work_hours_premise:
    # check if the working hours of Tina in the hypothesis contradicts the working hours of Tina in the premise
    label = "contradiction"
else:
    # if the working hours of Tina in the hypothesis does not contradict the working hours of Tina in the premise, we can infer entailment
    label = "entailment"

print(label)
