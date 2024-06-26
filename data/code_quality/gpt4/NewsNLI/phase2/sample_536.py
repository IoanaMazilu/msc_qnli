copies_sold_premise = 10000000
copies_sold_hypothesis = 10000000

# the hypothesis mentions the number of ''Brain Training'' copies sold worldwide, which is also referenced in the premise
if copies_sold_hypothesis != copies_sold_premise:
    # check if the number of copies sold in the hypothesis contradicts the number of copies sold reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
