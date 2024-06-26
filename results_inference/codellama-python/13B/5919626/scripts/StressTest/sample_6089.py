days_work_premise = 12
days_work_hypothesis = 72
days_work_remaining_premise = 10
days_work_remaining_hypothesis = 10

# the hypothesis talks about the number of days worked by Matt and Peter
if days_work_hypothesis <= days_work_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_work_premise'
    label = "contradiction"
elif days_work_remaining_hypothesis!= days_work_remaining_premise:
    # check if the number of days worked by Peter in the hypothesis contradicts the number of days worked by Peter in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
