ram_shyam_work_premise = 10
ram_shyam_work_hypothesis = 20

# the hypothesis refers to the number of days required to complete a piece of work
if ram_shyam_work_hypothesis <= ram_shyam_work_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ram_shyam_work_premise'
    label = "contradiction"
elif ram_shyam_work_premise!= ram_shyam_work_hypothesis:
    # check if the number of days in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
