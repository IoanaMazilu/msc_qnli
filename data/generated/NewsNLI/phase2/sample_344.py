# Premise: Samantha Pecoraro, 14, has a permanent feeding tube in her stomach because nearly all foods trigger a violent reaction in her digestive tracts.
# Hypothesis: Samantha, 14, gets her food only through her stomach feeding tube.
# Golden Label: entailment

age_premise = 14
age_hypothesis = 14

# the hypothesis mentions the age of Samantha and the way she eats, which are also referenced in the premise
# however, the hypothesis does not mention the reason why she eats in this manner, which is included in the premise
if age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age in the premise, we can't infer entailment or contradiction
    label = "neutral"

print(label)

