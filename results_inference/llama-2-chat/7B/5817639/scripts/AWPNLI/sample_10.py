served_cakes_premise = float(5.0) + float(6.0)
served_cakes_hypothesis = float(14.0)

# compare the number of cakes served in the hypothesis to the total number of cakes served in the premise
if served_cakes_hypothesis >= served_cakes_premise:
    # check if the number of cakes served in the hypothesis contradicts the total number of cakes served in the premise
    label = "contradiction"
elif served_cakes_hypothesis!= served_cakes_premise:
    # if the number of cakes served in the hypothesis does not contradict the total number of cakes served in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
