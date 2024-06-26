ram_krish_work_premise = 40
ram_krish_work_hypothesis = 40
bhim_work_premise = 40
bhim_work_hypothesis = 40

# the hypothesis refers to the number of days it takes for Ram and Krish to complete the work, which is also mentioned in the premise
if ram_krish_work_hypothesis <= ram_krish_work_premise:
    # check if the estimate of 'ram_krish_work_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif bhim_work_hypothesis!= bhim_work_premise:
    # check if the number of days it takes for Bhim to complete the work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
