germs_premise = 0.036 * (20 ** 5)
germs_hypothesis = 0.036 * (10 ** 5)
dishes_premise = 36000 * (10 ** -3)
dishes_hypothesis = 36000 * (10 ** -3)

# the hypothesis speaks about the number of germs and Petri dishes in the lab, which is also mentioned in the premise
if germs_hypothesis > germs_premise:
    # check if the number of germs in the hypothesis exceeds the number of germs in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
     # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
