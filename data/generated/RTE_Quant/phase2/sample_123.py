# Premise: Take consumer products giant Procter and Gamble. Even with a $1.8 billion Research and Development budget, it still manages 500 active partnerships each year, many of them with small companies.
# Hypothesis: Procter and Gamble spends $1.8 billion for Research and Development.
# Golden Label: entailment

rd_budget_premise = 1.8e9
rd_budget_hypothesis = 1.8e9

# the hypothesis talks about the Research and Development budget of Procter and Gamble, which is also mentioned in the premise
# the hypothesis does not contradict the premise, we can infer entailment
if rd_budget_hypothesis == rd_budget_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)

