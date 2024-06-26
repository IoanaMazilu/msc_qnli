apples_maddie_premise = 18
apples_given_premise = 22
apples_maddie_hypothesis = 48
apples_given_hypothesis = 22

# the hypothesis talks about the number of apples Maddie has and gives them away, also referenced in the premise
if apples_maddie_premise <= apples_maddie_hypothesis:
    # check if the estimate of 'apples_maddie_hypothesis' contradicts the number of apples Maddie has in the premise
    label = "contradiction"
elif apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples Maddie gives away in the hypothesis contradicts the number of apples given away in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
