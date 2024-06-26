parts_premise1 = 5
parts_premise2 = 6
parts_premise3 = 9
parts_hypothesis1 = 1
parts_hypothesis2 = 6
parts_hypothesis3 = 9

# the hypothesis refers to the number of equal parts that the herd can be divided into, mentioned in the premise
if parts_hypothesis1 >= parts_premise1:
    # check if the estimate of 'parts_hypothesis1' contradicts the number of parts in the premise
    label = "contradiction"
elif parts_hypothesis2 != parts_premise2 or parts_hypothesis3 != parts_premise3:
    # check if the number of parts in the hypothesis contradicts the number of parts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
