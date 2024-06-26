ramesh_premise = 60
ramesh_hypothesis = 20
sushil_premise = 25
sushil_hypothesis = 25

# the hypothesis refers to the number of days taken by Ramesh and Sushil to finish a work
if ramesh_hypothesis <= ramesh_premise:
    # check if the estimate of 'ramesh_hypothesis' contradicts the number of days taken by Ramesh in the premise
    label = "contradiction"
elif sushil_hypothesis!= sushil_premise:
    # check if the number of days taken by Sushil in the hypothesis contradicts the number of days taken by Sushil reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
