# Premise: In the biology lab of '' Jefferson'' High School there are 1.08 * 10 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 1.08 * less than 60 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Golden Label: entailment

germs_premise = 1.08 * 10**6
germs_hypothesis = 1.08 * 60**6
dishes_premise = 10800
dishes_hypothesis = 10800

# the hypothesis refers to the number of germs and dishes mentioned in the premise
if germs_hypothesis >= germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
elif dishes_hypothesis != dishes_premise:
    # check if the number of dishes in the hypothesis contradicts the number of dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

