# Premise: -LRB- CNN -RRB- -- Around 1,000 people accused of being witches in Gambia have been locked up in secret detention centers and forced to drink a dangerous hallucinogenic potion, according to human rights organization Amnesty International.
# Hypothesis: Victims forced to drink dangerous hallucinogenic potion ; at least two have died.
# Golden Label: entailment

accused_people_premise = 1000
deaths_hypothesis = 2

# the hypothesis refers to people being forced to drink a dangerous hallucinogenic potion, which is also mentioned in the premise
# however, the hypothesis also mentions deaths, which is not mentioned in the premise
label = "neutral"

print(label)

