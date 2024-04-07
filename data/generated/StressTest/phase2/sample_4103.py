# Premise: Peter has 9 candies, rina has 5 candies.
# Hypothesis: Peter has less than 9 candies, rina has 5 candies.
# Golden Label: contradiction

peter_candies_premise = 9
peter_candies_hypothesis = 9
rina_candies_premise = 5
rina_candies_hypothesis = 5

# the hypothesis talks about the number of candies Peter and Rina have, which is also referenced in the premise
if peter_candies_hypothesis < peter_candies_premise:
    # check if the hypothesis value contradicts the number of candies Peter has in the premise
    label = "contradiction"
elif rina_candies_hypothesis != rina_candies_premise:
    # check if the number of candies Rina has in the hypothesis contradicts the number of candies she has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

