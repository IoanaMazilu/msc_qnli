# Premise: In the biology lab of '' Jefferson'' High School there are 0.036 * 10 ^ 5 germs, equally divided among 18000 * 10 ^ (-3) Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 0.036 * less than 70 ^ 5 germs, equally divided among 18000 * 10 ^ (-3) Petri dishes.
# Golden Label: entailment

germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * 70 ** 5
dishes_premise = 18000 * 10 ** (-3)
dishes_hypothesis = 18000 * 10 ** (-3)

# the hypothesis talks about the number of germs and Petri dishes in the biology lab,
# which is also mentioned in the premise
if germs_hypothesis >= germs_premise:
    # check if the hypothesis estimate contradicts the number of germs in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we cannot infer entailment, since the hypothesis only gives a lower limit for the number of germs,
    # but does not confirm the exact number of germs as the premise does
    label = "neutral"

print(label)

