# Premise: Joan picked 37.0 oranges, and Sara picked 10.0 oranges and Alyssa picked 30.0 pears.
# Hypothesis: 48.0 oranges were picked in total.
# Golden Label: contradiction

joan_oranges_premise = 37.0
sara_oranges_premise = 10.0
total_oranges_hypothesis = 48.0

# the hypothesis refers to the total number of oranges picked, which are also mentioned in the premise
# compute the total number of oranges in the premise
total_oranges_premise = joan_oranges_premise + sara_oranges_premise
if total_oranges_hypothesis != total_oranges_premise:
    # check if the total number of oranges in the hypothesis contradicts the total number of oranges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

