 work_finish_premise = 7
work_finish_hypothesis = 7

# the hypothesis talks about the number of days Anita and Indu leave before the work is finished, which is also mentioned in the premise
if work_finish_hypothesis!= work_finish_premise:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
