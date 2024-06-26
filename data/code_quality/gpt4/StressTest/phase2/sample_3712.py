germs_premise = 5.4 * (70 ** 6)
germs_hypothesis = 5.4 * (10 ** 6)
dishes_premise = 10800
dishes_hypothesis = 10800

# the hypothesis refers to the number of germs and Petri dishes mentioned in the premise
if germs_hypothesis > germs_premise:
    # check if the number of germs in the hypothesis contradicts the number of germs reported in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
