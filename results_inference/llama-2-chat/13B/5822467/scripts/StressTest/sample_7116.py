germs_premise = 43200000
germs_hypothesis = 30000000
petri_dishes_premise = 10800

# the hypothesis refers to the number of germs and the number of petri dishes
if germs_hypothesis <= germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_premise!= petri_dishes_hypothesis:
    # check if the number of petri dishes in the hypothesis contradicts the number of petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
