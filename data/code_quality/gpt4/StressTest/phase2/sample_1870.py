germs_premise = 6.48 * (20 ** 6)
germs_hypothesis = 6.48 * (10 ** 6)
petri_dishes_premise = 10800
petri_dishes_hypothesis = 10800

# the hypothesis refers to the number of germs and Petri dishes mentioned in the premise
if germs_premise <= germs_hypothesis:
    # check if the number of germs in the hypothesis contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_hypothesis != petri_dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
