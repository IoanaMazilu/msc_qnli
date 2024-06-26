women_premise = 17
children_premise = 6
children_hypothesis = 6
women_hypothesis = 17

# the hypothesis mentions the number of women and children among the dead, which are also mentioned in the premise
if women_hypothesis!= women_premise or children_hypothesis!= children_premise:
    # check if the number of women or children in the hypothesis contradicts the number of women or children in the premise
    label = "contradiction"
else:
    # if the number of women and children in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
