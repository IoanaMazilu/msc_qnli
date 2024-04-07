# Premise: In the biology lab of '' Jefferson'' High School there are 6.48 * 10 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 6.48 * 60 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Golden Label: contradiction

germs_premise = 6.48 * 10 ** 6
germs_hypothesis = 6.48 * 60 ** 6
dishes_premise = 10800
dishes_hypothesis = 10800

# the hypothesis refers to the number of germs and dishes mentioned in the premise
if germs_premise != germs_hypothesis:
    # check if the number of germs in the hypothesis contradicts the number of germs reported in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
    # check if the number of dishes in the hypothesis contradicts the number of dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

