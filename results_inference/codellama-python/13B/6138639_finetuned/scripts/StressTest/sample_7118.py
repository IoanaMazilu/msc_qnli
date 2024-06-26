germs_premise = 4.32 * 10 ** 6
germs_hypothesis = 4.32 * 10 ** 6

# the hypothesis refers to the number of germs in the biology lab mentioned in the premise
if germs_hypothesis <= germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
