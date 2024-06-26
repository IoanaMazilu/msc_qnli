bookman_copies_premise = 60
bookman_copies_hypothesis = 40
bookman_hardback_premise = 10
bookman_hardback_hypothesis = 10
bookman_paperback_premise = 50
bookman_paperback_hypothesis = 50

# the hypothesis refers to the number of copies of the book purchased by Bookman
if bookman_copies_hypothesis <= bookman_copies_premise:
    # check if the hypothesis value contradicts the number of copies purchased in the premise
    label = "contradiction"
elif bookman_hardback_hypothesis!= bookman_hardback_premise:
    # check if the number of hardback copies in the hypothesis contradicts the number of hardback copies reported in the premise
    label = "contradiction"
elif bookman_paperback_hypothesis!= bookman_paperback_premise:
    # check if the number of paperback copies in the hypothesis contradicts the number of paperback copies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
