# Premise: In the biology lab of '' Jefferson'' High School there are 0.036 * 10 ^ 5 germs, equally divided among 18000 * 10 ^ (-3) Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 0.036 * 40 ^ 5 germs, equally divided among 18000 * 10 ^ (-3) Petri dishes.
# Golden Label: contradiction

germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * 40 ** 5
dishes_premise = 18000 * 10 ** (-3)
dishes_hypothesis = 18000 * 10 ** (-3)

# The hypothesis talks about the number of germs and petri dishes in the biology lab, which are also referenced in the premise
if germs_hypothesis != germs_premise:
    # Check if the number of germs in the hypothesis contradicts the number of germs reported in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
    # Check if the number of petri dishes in the hypothesis contradicts the number of petri dishes reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

