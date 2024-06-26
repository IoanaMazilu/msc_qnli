work_rohit_premise = 12
work_rohan_premise = 6
work_rohit_hypothesis = 22
work_rohan_hypothesis = 6

# the hypothesis refers to the time Rohit and Rohan need to complete the work, as mentioned in the premise
if work_rohit_premise >= work_rohit_hypothesis:
    # check if the estimate of 'work_rohit_hypothesis' contradicts the time Rohit needs to complete the work in the premise
    label = "contradiction"
elif work_rohan_premise!= work_rohan_hypothesis:
    # check if the time Rohan needs to complete the work in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
