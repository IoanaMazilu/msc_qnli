victims_women_premise = 2
victims_men_premise = 2
victims_women_hypothesis = 2
victims_men_hypothesis = 2

# the hypothesis mentions the number of women and men victims, which is also mentioned in the premise
if victims_women_hypothesis!= victims_women_premise:
    # check if the number of women victims in the hypothesis contradicts the number of women victims reported in the premise
    label = "contradiction"
elif victims_men_hypothesis!= victims_men_premise:
    # check if the number of men victims from the hypothesis contradicts the number of men victims in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
