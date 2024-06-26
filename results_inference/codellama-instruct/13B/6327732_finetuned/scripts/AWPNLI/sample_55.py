total_gems_premise = 5155.0
diamonds_premise = 45.0
rubies_premise = total_gems_premise - diamonds_premise

total_gems_hypothesis = 5108.0
rubies_hypothesis = total_gems_hypothesis - diamonds_premise

if rubies_hypothesis!= rubies_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
