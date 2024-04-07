# Premise: And just over half of the 88 women interviewed -- 46 of them -- live in fear of sexual assaults around the refugee camp.
# Hypothesis: 88 Darfuri women interviewed in Chad described'' profound'' suffering and fear.
# Golden Label: neutral

total_women_interviewed_premise = 88
women_living_in_fear_premise = 46
total_women_interviewed_hypothesis = 88

# the hypothesis mentions the total number of women interviewed, which matches the premise
# but, the premise also mentions the number of women living in fear around the refugee camp, which is not referenced in the hypothesis
# hence, we cannot infer entailment or contradiction based on the available data
label = "neutral"

print(label)
