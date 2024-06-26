% increase in bankruptcy filings_premise = 14
% increase in bankruptcy filings_hypothesis = 14

# the hypothesis and premise mention the percentage increase in bankruptcy filings
if % increase in bankruptcy filings_hypothesis!= % increase in bankruptcy filings_premise:
    # if the percentage increase in bankruptcy filings in the hypothesis contradicts the percentage increase in bankruptcy filings in the premise
    label = "contradiction"
else:
    # if the percentage increase in bankruptcy filings in the hypothesis and premise are the same
    label = "entailment"

print(label)
