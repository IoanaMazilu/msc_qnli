# Premise: Ramesh can finish a work in 20 days and Sushil in 25 days.
# Hypothesis: Ramesh can finish a work in more than 10 days and Sushil in 25 days.
# Golden Label: entailment

ramesh_premise = 20
ramesh_hypothesis = 10
sushil_premise = 25
sushil_hypothesis = 25

# the hypothesis refers to the time Ramesh and Sushil need to finish a work, mentioned in the premise
if ramesh_hypothesis >= ramesh_premise:
    # check if the estimate of 'ramesh_hypothesis' contradicts the time Ramesh needs to finish a work in the premise
    label = "contradiction"
elif sushil_hypothesis != sushil_premise:
    # check if the time Sushil needs to finish a work in the hypothesis contradicts the time Sushil needs to finish a work reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

