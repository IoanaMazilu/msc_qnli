# Premise: In the biology lab of '' Jefferson'' High School there are 4.32 * less than 30 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Hypothesis: In the biology lab of '' Jefferson'' High School there are 4.32 * 10 ^ 6 germs, equally divided among 10,800 Petri dishes.
# Golden Label: neutral

germs_premise = 4.32 * (30 ** 6) # calculate the total number of germs in the premise
germs_hypothesis = 4.32 * (10 ** 6) # calculate the total number of germs in the hypothesis
petri_dishes_premise = 10800
petri_dishes_hypothesis = 10800

# the hypothesis refers to the number of germs and petri dishes mentioned in the premise
if germs_hypothesis > germs_premise:
    # check if the number of germs in the hypothesis contradicts the number of germs estimated in the premise
    label = "contradiction"
elif petri_dishes_hypothesis != petri_dishes_premise:
    # check if the number of petri dishes in the hypothesis contradicts the number of petri dishes reported in the premise
    label = "contradiction"
elif germs_hypothesis < germs_premise and petri_dishes_hypothesis == petri_dishes_premise:
    # if the number of germs in the hypothesis is less than the estimate in the premise and the number of petri dishes is the same
    # we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but can't be explicitly entailed either
    # we infer it's neutral
    label = "neutral"

print(label)

