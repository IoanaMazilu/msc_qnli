# Premise: If the perimeter of Δ ACD is 9 + 3 √ 3, what is the perimeter of equilateral triangle Δ ABC?
# Hypothesis: If the perimeter of Δ ACD is 5 + 3 √ 3, what is the perimeter of equilateral triangle Δ ABC?
# Golden Label: contradiction

perimeter_ACD_premise = 9 + 3 * (3 ** 0.5)
perimeter_ACD_hypothesis = 5 + 3 * (3 ** 0.5)

# the hypothesis refers to the perimeter of triangle ACD mentioned in the premise
if perimeter_ACD_premise != perimeter_ACD_hypothesis:
    # check if the value of 'perimeter_ACD_hypothesis' contradicts the value of perimeter_ACD in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

