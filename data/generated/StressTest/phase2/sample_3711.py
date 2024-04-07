# Premise: In the biology lab of '' Jefferson'' High School there are 5.4 * 10 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 5.4 * less than 70 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Golden Label: entailment

germs_premise = 5.4 * (10 ** 6)
germs_hypothesis = 5.4 * (70 ** 6)
dishes_premise = 10800
dishes_hypothesis = 10800

# the hypothesis talks about the number of germs and petri dishes in the biology lab, also mentioned in the premise
if germs_hypothesis >= germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
    # check if the number of petri dishes in the hypothesis contradicts the number of petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

