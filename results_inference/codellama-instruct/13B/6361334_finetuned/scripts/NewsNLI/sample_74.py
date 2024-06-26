# define variables for the entities in the premise and hypothesis
president_premise = "Nicolas Maduro"
generals_premise = 3
president_hypothesis = "Nicolas Maduro"
generals_hypothesis = 3

# check if the president in the hypothesis is the same as the president in the premise
if president_hypothesis!= president_premise:
    # if the president in the hypothesis is not the same as the president in the premise, we cannot infer entailment or contradiction
    label = "neutral"
else:
    # if the president in the hypothesis is the same as the president in the premise, we can infer entailment
    label = "entailment"

print(label)
