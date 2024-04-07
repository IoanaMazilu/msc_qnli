# Premise: In the biology lab of '' Jefferson'' High School there are 3.24 * 10 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 3.24 * less than 30 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Golden Label: entailment

germs_premise = 3.24 * 10 ** 6
germs_hypothesis_estimate = 30 ** 6
dishes_premise = 10800
dishes_hypothesis = 10800

# the hypothesis speaks about the number of germs and Petri dishes in the lab, mentioned also in the premise
if germs_premise >= germs_hypothesis_estimate:
    # check if the number of germs in the premise contradicts the estimate of less than 'germs_hypothesis_estimate'
    label = "contradiction"
elif dishes_premise != dishes_hypothesis:
    # check if the number of Petri dishes in the premise contradicts the number of Petri dishes in the hypothesis
    label = "contradiction"
else:
    # the premise gives a specific number of germs and Petri dishes
    # any number of germs less than 'germs_hypothesis_estimate' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

