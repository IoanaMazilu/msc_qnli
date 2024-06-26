votes_counted_premise = 0.7
seats_won_premise = 149
total_seats_premise = 300
seats_won_hypothesis = 149

# the hypothesis mentions the number of seats won by Syriza, which is also mentioned in the premise
# however, the hypothesis does not mention the percentage of votes counted, which is specified in the premise
if seats_won_hypothesis != seats_won_premise:
    # check if the number of seats won in the hypothesis contradicts the number of seats won in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "neutral"

print(label)
