# Premise: Hari Dallakoti says business at his UPS store in Denver, Colorado, is down 25 percent.
# Hypothesis: UPS store owner says business down at least 25 percent.
# Golden Label: entailment

business_down_premise = 0.25
business_down_hypothesis = 0.25

# the hypothesis mentions the business down percentage which is also mentioned in the premise
if business_down_hypothesis > business_down_premise:
    # check if the business down percentage in the hypothesis is greater than the percentage reported in the premise
    label = "contradiction"
elif business_down_hypothesis < business_down_premise:
    # check if the business down percentage in the hypothesis is less than the percentage reported in the premise
    label = "contradiction"
else:
    # if the business down percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

