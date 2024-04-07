# Premise: Cook can divide his herd into 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Hypothesis: Cook can divide his herd into less than 6 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Golden Label: entailment

parts_premise1 = 5
parts_premise2 = 6

parts_hypothesis1 = 6
parts_hypothesis2 = 9

# the hypothesis talks about the number of parts Cook can divide his herd into, referenced also in the premise
if parts_hypothesis1 > parts_premise1 or parts_hypothesis1 > parts_premise2:
    # check if the parts_hypothesis1 value contradicts the estimate of 'parts_premise1' and 'parts_premise2'
    label = "contradiction"
elif parts_hypothesis2 == parts_premise2:
    # check if the parts_hypothesis2 value contradicts the premise statement that Cook cannot divide his herd into 9 equal parts
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

