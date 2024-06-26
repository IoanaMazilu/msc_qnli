work_time_renu_premise = 4
work_time_renu_and_suma_premise = 4
work_time_renu_hypothesis = 8
work_time_renu_and_suma_hypothesis = 4

# the hypothesis talks about the time Renu and Renu with Suma can do a piece of work, which is also mentioned in the premise
if work_time_renu_hypothesis <= work_time_renu_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_time_renu_premise'
    label = "contradiction"
elif work_time_renu_and_suma_hypothesis != work_time_renu_and_suma_premise:
    # check if the time in which Renu and Suma are doing the work in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
