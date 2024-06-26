total_copies_premise = 60
hardback_copies_premise = 10
paperback_copies_premise = 50
hardback_price_premise = 20
paperback_price_premise = 10

total_copies_hypothesis = 40
hardback_copies_hypothesis = 10
paperback_copies_hypothesis = 30
hardback_price_hypothesis = 20
paperback_price_hypothesis = 10

# the hypothesis refers to the number of copies and their prices mentioned in the premise
if total_copies_hypothesis <= total_copies_premise:
    # check if the estimate of 'total_copies_hypothesis' contradicts the number of copies in the premise
    label = "contradiction"
elif hardback_copies_hypothesis!= hardback_copies_premise or paperback_copies_hypothesis!= paperback_copies_premise:
    # check if the number of hardback or paperback copies in the hypothesis contradicts the number of each type of copies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
