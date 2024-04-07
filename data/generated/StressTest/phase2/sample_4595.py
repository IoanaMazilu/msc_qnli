# Premise: Sally wants to bake as many cakes as possible and has 27 cups of milk and 18 cups of flour.
# Hypothesis: Sally wants to bake as many cakes as possible and has less than 27 cups of milk and 18 cups of flour.
# Golden Label: contradiction

milk_cups_premise = 27
flour_cups_premise = 18
milk_cups_hypothesis = 27
flour_cups_hypothesis = 18

# the hypothesis refers to the number of cups of milk and flour mentioned in the premise
if milk_cups_hypothesis >= milk_cups_premise:
    # check if the estimate of 'milk_cups_hypothesis' contradicts the number of milk cups in the premise
    label = "contradiction"
elif flour_cups_hypothesis != flour_cups_premise:
    # check if the number of flour cups in the hypothesis contradicts the number of flour cups reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

