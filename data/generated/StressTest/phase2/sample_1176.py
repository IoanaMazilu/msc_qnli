# Premise: Colin has an app on his phone that generates a random integer betwen 1 and 10.
# Hypothesis: Colin has an app on his phone that generates a random integer betwen less than 6 and 10.
# Golden Label: entailment

lower_bound_premise = 1
upper_bound_premise = 10
lower_bound_hypothesis = 6
upper_bound_hypothesis = 10

# the hypothesis refers to the range of random numbers generated by the app mentioned in the premise
if lower_bound_hypothesis < lower_bound_premise or upper_bound_hypothesis != upper_bound_premise:
    # check if the range of random numbers in the hypothesis contradicts the range specified in the premise
    label = "contradiction"
elif lower_bound_hypothesis == lower_bound_premise and upper_bound_hypothesis == upper_bound_premise:
    # if the range defined in the hypothesis completely matches the range in the premise, we can infer entailment
    label = "entailment"
else:
    # if the range in the hypothesis is only a subset of the range in the premise, it does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
