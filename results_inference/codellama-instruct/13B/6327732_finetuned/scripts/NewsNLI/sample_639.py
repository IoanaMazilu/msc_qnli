favorable_view_premise = 0.15
favorable_view_hypothesis = 0.10

# the hypothesis mentions the percentage of Saudis with a favorable view of al Qaeda, which is also mentioned in the premise
# however, the hypothesis refers to a different group of people (Saudis) than the premise (people who have a favorable view of al Qaeda's leader, Saudi exile Osama bin Laden)
# therefore, we cannot infer entailment or contradiction
label = "neutral"

print(label)
