renu_work_premise = 6
renu_suma_work_premise = 3
renu_work_hypothesis = 5
renu_suma_work_hypothesis = 3

# the hypothesis refers to the time Renu takes to do a piece of work alone and with her friend Suma, both mentioned in the premise
if renu_work_hypothesis < renu_work_premise:
    # check if the estimate of 'renu_work_hypothesis' contradicts the time Renu takes to do the work alone in the premise
    label = "contradiction"
elif renu_suma_work_hypothesis != renu_suma_work_premise:
    # check if the time Renu and Suma take to do the work in the hypothesis contradicts the time they take in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
