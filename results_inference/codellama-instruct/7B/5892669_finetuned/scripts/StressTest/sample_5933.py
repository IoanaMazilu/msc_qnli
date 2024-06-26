herd_division_premise_1 = 5
herd_division_premise_2 = 6
herd_division_premise_3 = 9

herd_division_hypothesis_1 = 5
herd_division_hypothesis_2 = 6
herd_division_hypothesis_3 = 9

# the hypothesis refers to the number of equal parts Antony can divide his herd into, mentioned in the premise
if herd_division_hypothesis_1 >= herd_division_premise_1:
    # check if the estimate of 'herd_division_hypothesis_1' contradicts the number of equal parts in the premise
    label = "contradiction"
elif herd_division_hypothesis_2!= herd_division_premise_2:
    # check if the number of equal parts in the hypothesis contradicts the number of equal parts reported in the premise
    label = "contradiction"
elif herd_division_hypothesis_3!= herd_division_premise_3:
    # check if the number of equal parts in the hypothesis contradicts the number of equal parts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
