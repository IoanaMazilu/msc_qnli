# Premise: 75 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Hypothesis: 25 percent of Andrea's living room floor is covered by a carpet that is 4 feet by 9 feet.
# Golden Label: contradiction

percentage_covered_premise = 75
percentage_covered_hypothesis = 25
carpet_size = 4 * 9 # both premise and hypothesis refer to the same carpet size

# the hypothesis refers to the percentage of floor covered by the carpet, which is mentioned in the premise
if percentage_covered_hypothesis > percentage_covered_premise:
    # check if the coverage percentage in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif percentage_covered_hypothesis < percentage_covered_premise:
    # the premise gives a larger coverage percentage
    # a smaller percentage is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

