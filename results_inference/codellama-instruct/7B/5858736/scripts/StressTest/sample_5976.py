germs_premise = 0.036 * 10 ^ 5
germs_hypothesis = 0.036 * 79 ^ 5
petri_dishes_premise = 75000 * 10 ^ (-3)
petri_dishes_hypothesis = 75000 * 10 ^ (-3)

# the hypothesis refers to the number of germs and petri dishes mentioned in the premise
if germs_hypothesis <= germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_hypothesis!= petri_dishes_premise:
    # check if the number of petri dishes in the hypothesis contradicts the number of petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
