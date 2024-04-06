# Premise: Isha’s pencil is 12.0 cubes long, and she gets another pencil that is 12.0 cubes long.
# Hypothesis: Both pencils are 26.0 cubes long.
# Golden Label: contradiction

first_pencil_premise = 12.0
second_pencil_premise = 12.0
both_pencils_length_hypothesis = 26.0

# the hypothesis makes a statement about the total length of both pencils, which are individually mentioned in the premise
# compute the total length of both pencils in the premise
both_pencils_length_premise = first_pencil_premise + second_pencil_premise
if both_pencils_length_hypothesis != both_pencils_length_premise:
    # check if the total length of pencils in the hypothesis contradicts the total length of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

