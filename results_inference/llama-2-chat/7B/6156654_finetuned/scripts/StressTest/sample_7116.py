germs_premise = 4.32e6
germs_hypothesis = 30e6
petri_dishes = 10800

# the hypothesis refers to the number of germs, which is also mentioned in the premise
if germs_hypothesis <= germs_premise:
    # check if the number of germs in the hypothesis contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes!= 10800:
    # check if the number of petri dishes in the hypothesis contradicts the number of petri dishes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
