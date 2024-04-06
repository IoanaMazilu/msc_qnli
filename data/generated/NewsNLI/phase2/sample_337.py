# Premise: So far, 283 people have been killed and two people are missing in Thailand, according to the government website Thaiflood.com.
# Hypothesis: Thai floods have so far killed 283 people ; two people remain missing.
# Golden Label: entailment

people_killed_premise = 283
people_missing_premise = 2
people_killed_hypothesis = 283
people_missing_hypothesis = 2

# the hypothesis mentions the number of people killed and missing due to Thai floods, which are also mentioned in the premise
if people_killed_hypothesis != people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed reported in the premise
    label = "contradiction"
elif people_missing_hypothesis != people_missing_premise:
    # check if the number of people missing from the hypothesis contradicts the number of people missing in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

