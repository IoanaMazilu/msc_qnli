total_copies_premise = 60
total_copies_hypothesis = 40
hardback_premise = 10
hardback_hypothesis = 10
paperback_premise = total_copies_premise - hardback_premise
paperback_hypothesis = total_copies_hypothesis - hardback_hypothesis

# the hypothesis refers to the number of copies and types of books purchased by Bookman
if total_copies_hypothesis < total_copies_premise:
    # check if the number of copies in the hypothesis contradicts the number of copies in the premise
    label = "contradiction"
elif hardback_hypothesis!= hardback_premise:
    # check if the number of hardback books in the hypothesis contradicts the number of hardback books in the premise
    label = "contradiction"
elif paperback_hypothesis!= paperback_premise:
    # check if the number of paperback books in the hypothesis contradicts the number of paperback books in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
