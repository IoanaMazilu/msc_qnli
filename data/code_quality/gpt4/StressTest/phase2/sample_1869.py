germs_premise = 6.48 * 10 ** 6
germs_hypothesis = 6.48 * 20 ** 6
dishes_premise = 10800
dishes_hypothesis = 10800

# checking the number of germs and dishes in the lab as stated in the premise and hypothesis
if germs_hypothesis >= germs_premise:
    # checking if the estimated number of germs in the hypothesis contradicts the stated number in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
    # checking if the number of dishes in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
