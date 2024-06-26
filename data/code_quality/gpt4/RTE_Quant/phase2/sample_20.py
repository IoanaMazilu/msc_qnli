wars_premise = 3
wars_over_kashmir_premise = 2
wars_hypothesis = 3

# the hypothesis talks about the number of wars India and Pakistan fought over Kashmir
# the premise also mentions the number of wars fought and the number of those that were for Kashmir
if wars_hypothesis != wars_premise:
    # check if the total number of wars in the hypothesis contradicts the total number of wars from the premise
    label = "contradiction"
elif wars_over_kashmir_premise != wars_hypothesis:
    # check if the number of wars over Kashmir in the hypothesis contradicts the number of wars over Kashmir in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
