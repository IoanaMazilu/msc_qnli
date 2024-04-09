bookman_copies_premise = 60
bookman_copies_hypothesis = 50
hardback_copies_premise = 10
hardback_copies_hypothesis = 10
paperback_copies_premise = 50
paperback_copies_hypothesis = 40

# the hypothesis refers to the number of copies purchased and the types of books mentioned in the premise
if bookman_copies_hypothesis <= bookman_copies_premise:
    # check if the estimate of 'bookman_copies_hypothesis' contradicts the number of copies purchased in the premise
    label = "contradiction"
elif hardback_copies_hypothesis!= hardback_copies_premise:
    # check if the number of hardback copies in the hypothesis contradicts the number of hardback copies reported in the premise
    label = "contradiction"
elif paperback_copies_hypothesis!= paperback_copies_premise:
    # check if the number of paperback copies in the hypothesis contradicts the number of paperback copies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
