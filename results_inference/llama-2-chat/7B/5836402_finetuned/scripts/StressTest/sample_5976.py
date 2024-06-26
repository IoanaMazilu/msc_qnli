germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * (less than 80 ** 5)
dishes_premise = 75000 * 10 ** (-3)
dishes_hypothesis = 75000 * 10 ** (-3)

# the hypothesis refers to the number of germs and dishes mentioned in the premise
if germs_premise!= germs_hypothesis:
    # check if the number of germs in the hypothesis contradicts the number of germs reported in the premise
    label = "contradiction"
elif dishes_hypothesis!= dishes_premise:
    # check if the number of dishes in the hypothesis contradicts the number of dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
