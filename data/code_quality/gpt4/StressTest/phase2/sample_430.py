england_france_premise = 22
england_france_hypothesis = 12
england_italy_premise = 6
england_italy_hypothesis = 6
france_italy_premise = 0
france_italy_hypothesis = 0

# the hypothesis talks about the number of club members who traveled to specific pairs of countries, referenced also in the premise
if england_france_hypothesis >= england_france_premise:
    # check if the hypothesis value contradicts the estimate of less than 'england_france_premise'
    label = "contradiction"
elif england_italy_hypothesis != england_italy_premise:
    # check if the number of members traveling to England and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif france_italy_hypothesis != france_italy_premise:
    # check if the number of members traveling to France and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
