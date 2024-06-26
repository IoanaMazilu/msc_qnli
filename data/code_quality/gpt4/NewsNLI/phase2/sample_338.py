people_in_prostitution_premise = 80000
women_trafficked_premise = 4000

women_trafficked_hypothesis = 4000

# the hypothesis mentions the number of trafficked women for sexual exploitation in the UK, which is also referenced in the premise
if women_trafficked_hypothesis != women_trafficked_premise:
    # check if the number of trafficked women in the hypothesis contradicts the number of trafficked women reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
