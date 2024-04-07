# Premise: In the biology lab of '' Jefferson'' High School there are 0.036 * 10 ^ 5 germs, equally divided among 36000 * 10 ^ (-3) Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 0.036 * less than 20 ^ 5 germs, equally divided among 36000 * 10 ^ (-3) Petri dishes.
# Golden Label: entailment

germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * 20 ** 5
dishes_premise = 36000 * 10 ** (-3)
dishes_hypothesis = 36000 * 10 ** (-3)

# the hypothesis refers to the number of germs and Petri dishes mentioned in the premise
if dishes_premise != dishes_hypothesis:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes reported in the premise
    label = "contradiction"
elif germs_hypothesis >= germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

