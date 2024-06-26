ramesh_work_premise = 60
sushil_work_premise = 25
ramesh_work_hypothesis = 20
sushil_work_hypothesis = 25

# the hypothesis talks about the number of days Ramesh and Sushil need to finish a work
if ramesh_work_hypothesis >= ramesh_work_premise:
    # check if the number of days Ramesh needs to finish a work in the hypothesis contradicts the estimate of less than 'ramesh_work_premise'
    label = "contradiction"
elif sushil_work_hypothesis!= sushil_work_premise:
    # check if the number of days Sushil needs to finish a work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
