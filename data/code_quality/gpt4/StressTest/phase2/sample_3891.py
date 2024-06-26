albert_work_premise = 20
albert_work_hypothesis = 50
rose_work_premise = 30
rose_work_hypothesis = 30

# the hypothesis refers to the time Albert and Rose need to complete a piece of work, mentioned also in the premise
if albert_work_hypothesis < albert_work_premise:
    # check if the estimate of 'albert_work_hypothesis' contradicts the time Albert needs to complete the work in the premise
    label = "contradiction"
elif rose_work_hypothesis != rose_work_premise:
    # check if the time Rose needs to complete the work in the hypothesis contradicts the time Rose needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
