copies_purchased_premise = 60
copies_purchased_hypothesis = 60
hardback_copies_premise = 10
hardback_copies_hypothesis = 10
paperback_copies_premise = 50
paperback_copies_hypothesis = 50

# the hypothesis refers to the number of copies purchased and their types, which are also mentioned in the premise
if copies_purchased_hypothesis >= copies_purchased_premise:
    # check if the number of copies in the hypothesis contradicts the number of copies purchased in the premise
    label = "contradiction"
elif hardback_copies_hypothesis!= hardback_copies_premise:
    # check if the number of hardback copies in the hypothesis contradicts the number of hardback copies in the premise
    label = "contradiction"
elif paperback_copies_hypothesis!= paperback_copies_premise:
    # check if the number of paperback copies in the hypothesis contradicts the number of paperback copies in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
