# Premise: In the biology lab of '' Jefferson'' High School there are 5.4 * 10 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 5.4 * more than 10 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Golden Label: contradiction

germs_premise = 5.4 * 10 ** 6
germs_hypothesis = 5.4 * 10 ** 6 # since the hypothesis claims there are more than this number
petri_dishes_premise = 10800
petri_dishes_hypothesis = 10800

# the hypothesis refers to the number of germs and petri dishes in the premise
if germs_hypothesis > germs_premise:
    # check if the estimate of 'germs_hypothesis' contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_hypothesis != petri_dishes_premise:
    # check if the number of petri dishes in the hypothesis contradicts the number of petri dishes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we cannot infer entailment nor contradiction
    label = "neutral"

print(label)

