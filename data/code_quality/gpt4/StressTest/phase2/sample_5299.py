germs_premise = 0.036 * (70 ** 5)
germs_hypothesis = 0.036 * (10 ** 5)
dishes_premise = 18000 * (10 ** -3)
dishes_hypothesis = 18000 * (10 ** -3)

# the hypothesis refers to the number of germs and dishes in the premise
if germs_premise != germs_hypothesis:
    # check if the number of germs in the hypothesis contradicts the number of germs reported in the premise
    label = "contradiction"
elif dishes_premise != dishes_hypothesis:
    # check if the number of dishes in the hypothesis contradicts the number of dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
