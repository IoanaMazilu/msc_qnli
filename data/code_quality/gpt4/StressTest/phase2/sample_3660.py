total_votes_premise = 2000
total_votes_hypothesis = 2000
percent_votes_james_premise = 5
percent_votes_james_hypothesis = 4

# the hypothesis refers to the percent of votes James received in the premise
# first convert the percent to total votes
votes_james_premise = (percent_votes_james_premise / 100) * total_votes_premise
votes_james_hypothesis = (percent_votes_james_hypothesis / 100) * total_votes_hypothesis

if total_votes_hypothesis != total_votes_premise:
    # check if the total votes number in the hypothesis contradicts the total votes number in the premise
    label = "contradiction"
elif votes_james_hypothesis >= votes_james_premise:
    # check if the number of votes for James in the hypothesis contradicts the number of votes for James in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
