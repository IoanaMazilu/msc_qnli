# Premise: An estimated 35.8 million people are enslaved, according to the Global Slavery Index.
# Hypothesis: Global Slavery Index:More than 35 million people are in bondage worldwide.
# Golden Label: entailment

enslaved_people_premise = 35800000
enslaved_people_hypothesis = 35000000

# the hypothesis mentions the number of people enslaved worldwide, which is also mentioned in the premise
if enslaved_people_hypothesis > enslaved_people_premise:
    # check if the number of enslaved people in the hypothesis exceeds the number reported in the premise
    label = "contradiction"
else:
    # if the number of enslaved people in the hypothesis does not exceed the number from the premise, we can infer entailment
    label = "entailment"

print(label)

