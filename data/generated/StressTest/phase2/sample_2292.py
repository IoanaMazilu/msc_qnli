# Premise: The ages of Krish and Vaibhav are in the proportion of 3:5.
# Hypothesis: The ages of Krish and Vaibhav are in the proportion of less than 8:5.
# Golden Label: entailment

krish_vaibhav_proportion_premise = 3 / 5
krish_vaibhav_proportion_hypothesis = 8 / 5

# the hypothesis is about the age ratio of Krish and Vaibhav, which is also discussed in the premise
if krish_vaibhav_proportion_hypothesis <= krish_vaibhav_proportion_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
elif krish_vaibhav_proportion_hypothesis > krish_vaibhav_proportion_premise:
    # the premise specifies an exact age ratio for Krish and Vaibhav
    # any ratio greater than 'krish_vaibhav_proportion_premise' does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)

