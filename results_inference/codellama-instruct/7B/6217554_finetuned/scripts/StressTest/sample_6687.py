copies_book_premise = 60
copies_book_hypothesis = 40
hardback_copies_premise = 10
hardback_copies_hypothesis = 10
hardback_price_premise = 20
hardback_price_hypothesis = 20
paperback_copies_premise = 50
paperback_copies_hypothesis = 50
paperback_price_premise = 10
paperback_price_hypothesis = 10

# the hypothesis refers to the number of copies and the price of each copy mentioned in the premise
if copies_book_hypothesis >= copies_book_premise:
    # check if the number of copies in the hypothesis contradicts the number of copies reported in the premise
    label = "contradiction"
elif hardback_copies_hypothesis!= hardback_copies_premise:
    # check if the number of hardback copies in the hypothesis contradicts the number of hardback copies reported in the premise
    label = "contradiction"
elif hardback_price_hypothesis!= hardback_price_premise:
    # check if the price of hardback copies in the hypothesis contradicts the price of hardback copies reported in the premise
    label = "contradiction"
elif paperback_copies_hypothesis!= paperback_copies_premise:
    # check if the number of paperback copies in the hypothesis contradicts the number of paperback copies reported in the premise
    label = "contradiction"
elif paperback_price_hypothesis!= paperback_price_premise:
    # check if the price of paperback copies in the hypothesis contradicts the price of paperback copies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
