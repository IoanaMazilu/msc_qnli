germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * (less_than_80 ** 5)

# the hypothesis refers to the number of germs, which is also mentioned in the premise
if germs_hypothesis!= germs_premise:
    # check if the number of germs in the hypothesis contradicts the number of germs in the premise
    label = "contradiction"
else:
    # if the number of germs in the hypothesis does not contradict the number of germs in the premise, we can infer entailment
    label = "entailment"

print(label)
