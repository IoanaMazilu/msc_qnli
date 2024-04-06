# Premise: The government estimates around 80,000 people are involved in prostitution in Britain, with about 4,000 women having been trafficked for sexual exploitation.
# Hypothesis: UK government:Around 4,000 women trafficked in the UK for sexual exploitation.
# Golden Label: entailment

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

