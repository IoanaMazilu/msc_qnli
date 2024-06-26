women_premise = 17
children_premise = 6
women_hypothesis = 17
children_hypothesis = 6

# the hypothesis mentions the number of women and children among the dead, which are also mentioned in the premise
if women_hypothesis!= women_premise:
    # check if the number of women in the hypothesis contradicts the number of women reported in the premise
    label = "contradiction"
elif children_hypothesis!= children_premise:
    # check if the number of children from the hypothesis contradicts the number of children in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)