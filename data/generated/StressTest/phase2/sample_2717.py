# Premise: In the biology lab of '' Jefferson'' High School there are 3.24 * 10 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 3.24 * 60 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Golden Label: contradiction

germs_premise = 3.24 * 10 ** 6
germs_hypothesis = 3.24 * 60 ** 6
petri_dishes_premise = 10800
petri_dishes_hypothesis = 10800

# the hypothesis refers to the number of germs and Petri dishes mentioned in the premise
if germs_premise != germs_hypothesis:
    # check if the number of germs in the hypothesis contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_hypothesis != petri_dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

