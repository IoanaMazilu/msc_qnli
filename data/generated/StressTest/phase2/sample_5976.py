# Premise: In the biology lab of '' Jefferson'' High School there are 0.036 * 10 ^ 5 germs, equally divided among 75000 * 10 ^ (-3) Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 0.036 * less than 80 ^ 5 germs, equally divided among 75000 * 10 ^ (-3) Petri dishes.
# Golden Label: entailment

germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * 80 ** 5
dishes_premise = 75000 * 10 ** (-3)
dishes_hypothesis = 75000 * 10 ** (-3)

# the hypothesis refers to the number of germs and dishes in the premise
if germs_hypothesis >= germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
    # check if the number of dishes in the hypothesis contradicts the number of dishes reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of germs and dishes
    # the number of germs in the hypothesis is less than the number of germs in the premise
    label = "entailment"

print(label)

