men_suits_premise = 14797.0
women_suits_premise = 4969.0
total_suits_hypothesis = 19766.0

# compute the total number of suits in the premise
total_suits_premise = men_suits_premise + women_suits_premise

if total_suits_hypothesis > total_suits_premise:
    # the hypothesis implies that there are more suits available overall, which is an entailment
    label = "entailment"
elif total_suits_hypothesis < total_suits_premise:
    # the hypothesis implies that there are fewer suits available overall, which is a contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
