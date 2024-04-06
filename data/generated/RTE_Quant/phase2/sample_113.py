# Premise: Take consumer products giant Procter and Gamble. Even with a $1.8 billion Research and Development budget, it still manages 500 active partnerships each year, many of them with small companies.
# Hypothesis: 500 small companies are partners of Procter and Gamble.
# Golden Label: neutral

budget_premise = 1.8e9
partnerships_premise = 500
partnerships_hypothesis = 500

# the hypothesis talks about the number of partnerships with small companies, which is not detailed in the premise
# the premise only mentions the total number of partnerships, not specifically with small companies
# the hypothesis cannot be fully entailed from the premise, since we don't know the exact number of partnerships with small companies
label = "neutral"

print(label)

