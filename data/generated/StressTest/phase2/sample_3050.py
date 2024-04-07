# Premise: Rob has 8 toy trucks.
# Hypothesis: Rob has 5 toy trucks.
# Golden Label: contradiction

toy_trucks_premise = 8
toy_trucks_hypothesis = 5

# the hypothesis refers to the number of toy trucks Rob has, mentioned in the premise
if toy_trucks_hypothesis != toy_trucks_premise:
    # check if the number of toy trucks in the hypothesis contradicts the number of toy trucks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

