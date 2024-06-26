total_copies_premise = 60
hardback_copies_premise = 10
paperback_copies_premise = 50
hardback_price_premise = 20
paperback_price_premise = 10

total_copies_hypothesis = 60
hardback_copies_hypothesis = 10
paperback_copies_hypothesis = 50
hardback_price_hypothesis = 20
paperback_price_hypothesis = 10

# the hypothesis refers to the number of copies, hardback/paperback ratio, and prices mentioned in the premise
if total_copies_hypothesis > total_copies_premise:
    # check if the estimate of 'total_copies_hypothesis' contradicts the number of copies in the premise
    label = "contradiction"
elif hardback_copies_hypothesis!= hardback_copies_premise or paperback_copies_hypothesis!= paperback_copies_premise or hardback_price_hypothesis!= hardback_price_premise or paperback_price_hypothesis!= paperback_price_premise:
    # check if the hardback/paperback ratio, prices in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
