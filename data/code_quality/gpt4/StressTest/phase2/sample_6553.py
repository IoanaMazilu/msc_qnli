england_travelers_premise = 70
england_travelers_hypothesis = 30
france_travelers_premise = 26
france_travelers_hypothesis = 26
italy_travelers_premise = 32
italy_travelers_hypothesis = 32

# the hypothesis refers to the number of club members who traveled to England, France and Italy last year, also mentioned in the premise
if england_travelers_hypothesis >= england_travelers_premise:
    # check if the hypothesis value contradicts the estimate of less than 'england_travelers_premise'
    label = "contradiction"
elif france_travelers_hypothesis != france_travelers_premise:
    # check if the number of travelers to France in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif italy_travelers_hypothesis != italy_travelers_premise:
    # check if the number of travelers to Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
