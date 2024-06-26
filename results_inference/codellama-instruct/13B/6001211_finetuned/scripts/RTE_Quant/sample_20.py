wars_premise = 2
total_wars_premise = 3
wars_hypothesis = 3
total_wars_hypothesis = 3

# the hypothesis talks about the total number of wars between India and Pakistan for the possession of Kashmir
# the premise also mentions the same but specifies that two such wars have been fought
if wars_hypothesis!= total_wars_premise:
    # check if the total number of wars in the hypothesis contradicts the total number of wars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
