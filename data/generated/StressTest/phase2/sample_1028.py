# Premise: Mary can divide his herd into 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Hypothesis: Mary can divide his herd into less than 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Golden Label: contradiction

parts_premise_1 = 5
parts_premise_2 = 6
parts_premise_3 = 9
parts_hypothesis_1 = 5
parts_hypothesis_2 = 6
parts_hypothesis_3 = 9

# the hypothesis talks about the number of equal parts Mary can divide his herd into, referenced also in the premise
if parts_hypothesis_1 >= parts_premise_1:
    # check if the hypothesis value contradicts the premise of less than 'parts_hypothesis_1' equal parts
    label = "contradiction"
elif parts_hypothesis_2 != parts_premise_2 or parts_hypothesis_3 != parts_premise_3:
    # Check if the number of parts in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

