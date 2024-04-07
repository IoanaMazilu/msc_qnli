# Premise: Shreehari has 500 chocolates in his self.
# Hypothesis: Shreehari has less than 500 chocolates in his self.
# Golden Label: contradiction

chocolates_premise = 500
chocolates_hypothesis = 500

# the hypothesis refers to the number of chocolates Shreehari has, as mentioned in the premise
if chocolates_hypothesis >= chocolates_premise:
    # check if the hypothesis number contradicts the premise's statement that Shreehari has 'less than chocolates_premise' chocolates
    label = "contradiction"
else:
    # if the hypothesis number of chocolates does not contradict the premise's estimate, we can infer entailment
    label = "entailment"

print(label)

