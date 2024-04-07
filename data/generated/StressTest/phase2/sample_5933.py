# Premise: Antony can divide his herd into 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Hypothesis: Antony can divide his herd into less than 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Golden Label: contradiction

parts_division_premise = 5
parts_division_hypothesis = 5
parts_division_premise_2 = 6
parts_division_hypothesis_2 = 6
parts_division_premise_3 = 9
parts_division_hypothesis_3 = 9

# the hypothesis talks about parts Antony can divide his herd into, exactly as the premise does
if parts_division_hypothesis >= parts_division_premise:
    # check if the estimate of 'parts_division_hypothesis' contradicts the number of divisions in the premise
    label = "contradiction"
elif parts_division_hypothesis_2 != parts_division_premise_2:
    # check if the number of divisions in the hypothesis contradicts the number of divisions reported in the premise
    label = "contradiction"
elif parts_division_hypothesis_3 != parts_division_premise_3:
    # check if the number of divisions in the hypothesis contradicts the number of divisions reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

