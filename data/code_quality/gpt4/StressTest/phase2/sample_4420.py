tees_premise = 50
tees_hypothesis = 10
generic_tees_premise = 1
generic_tees_hypothesis = 1

# the hypothesis refers to the number of tees Bill must purchase, which is also mentioned in the premise
if tees_premise != tees_hypothesis:
    # check if the number of tees in the hypothesis contradicts the number of tees mentioned in the premise
    label = "contradiction"
elif generic_tees_premise != generic_tees_hypothesis:
    # check if the number of generic tees in the hypothesis contradicts the number of generic tees mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
