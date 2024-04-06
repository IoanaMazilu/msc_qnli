# Premise: Personal Bankruptcy Filings up 14% in first 6 months of 2010.
# Hypothesis: Consumer Bankruptcy Filings Up 14 Percent Through First Half Of 2010.
# Golden Label: entailment

percentage_increase_premise = 14
percentage_increase_hypothesis = 14
months_premise = 6
months_hypothesis = 6

# the hypothesis and premise mention the percentage increase of bankruptcy filings and the number of months into the year
if percentage_increase_hypothesis != percentage_increase_premise:
    # check if the percentage increase in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
elif months_hypothesis != months_premise:
    # check if the number of months in the hypothesis contradicts the number of months in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

