# Premise: Shreehari has 500 chocolates in his self.
# Hypothesis: Shreehari has more than 200 chocolates in his self.
# Golden Label: entailment

chocolates_premise = 500
chocolates_hypothesis = 200

# the hypothesis refers to the number of chocolates Shreehari has, also mentioned in the premise
if chocolates_premise <= chocolates_hypothesis:
    # check if the number of chocolates in the hypothesis contradicts the number of chocolates in the premise
    label = "contradiction"
else:
    # if the number of chocolates in the hypothesis is less than the number in the premise, we can infer entailment
    label = "entailment"

print(label)

