premise_hardback_copies = 10
premise_hardback_price = 20
premise_paperback_copies = 50
premise_paperback_price = 10
premise_total_copies = 60
premise_total_price = 1200

hypothesis_hardback_copies = 10
hypothesis_hardback_price = 20
hypothesis_paperback_copies = 50
hypothesis_paperback_price = 10
hypothesis_total_copies = 60
hypothesis_total_price = 1200

# check if the hypothesis values contradict the premise ones
if hypothesis_total_copies > premise_total_copies:
    label = "contradiction"
elif hypothesis_total_price > premise_total_price:
    label = "contradiction"
elif hypothesis_hardback_copies > premise_hardback_copies:
    label = "contradiction"
elif hypothesis_hardback_price > premise_hardback_price:
    label = "contradiction"
elif hypothesis_paperback_copies > premise_paperback_copies:
    label = "contradiction"
elif hypothesis_paperback_price > premise_paperback_price:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
