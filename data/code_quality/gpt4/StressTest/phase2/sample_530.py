germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * 50 ** 5
petri_dishes_premise = 45000 * 10 ** (-3)
petri_dishes_hypothesis = 45000 * 10 ** (-3)

# the hypothesis refers to the number of germs and Petri dishes mentioned in the premise
if germs_premise != germs_hypothesis:
    # check if the number of germs in the hypothesis contradicts the number of germs reported in the premise
    label = "contradiction"
elif petri_dishes_hypothesis != petri_dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
