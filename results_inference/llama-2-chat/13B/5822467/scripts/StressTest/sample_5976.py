germs_premise = 0.036 * 10^5
germs_hypothesis = 0.036 * less than 80^5
petri_dishes_premise = 75000 * 10^-3

# the hypothesis refers to the number of germs and the number of Petri dishes
if germs_hypothesis <= germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_premise!= petri_dishes_hypothesis:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
