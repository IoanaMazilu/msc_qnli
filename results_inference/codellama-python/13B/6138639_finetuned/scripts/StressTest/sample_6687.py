book_copies_premise = 60
book_copies_hypothesis = 40
hardback_copies_premise = 10
hardback_copies_hypothesis = 10
paperback_copies_premise = 60 - hardback_copies_premise
paperback_copies_hypothesis = 60 - hardback_copies_hypothesis

# the hypothesis refers to the number of book copies and their types mentioned in the premise
if book_copies_premise <= book_copies_hypothesis:
    # check if the estimate of 'book_copies_hypothesis' contradicts the number of book copies in the premise
    label = "contradiction"
elif hardback_copies_hypothesis!= hardback_copies_premise or paperback_copies_hypothesis!= paperback_copies_premise:
    # check if the number of hardback or paperback copies in the hypothesis contradicts the number of hardback or paperback copies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
