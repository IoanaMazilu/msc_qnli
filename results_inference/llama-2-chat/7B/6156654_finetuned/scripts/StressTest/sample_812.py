# defining the speeds of Sacha and Bruno
sacha_speed = 6
bruno_speed = 5

# defining the speeds in the hypothesis
sacha_speed_hypothesis = 3
bruno_speed_hypothesis = 5

# checking if the speeds in the hypothesis contradict the speeds in the premise
if sacha_speed_hypothesis!= sacha_speed or bruno_speed_hypothesis!= bruno_speed:
    # if the speeds in the hypothesis contradict the speeds in the premise, we can infer entailment
    label = "entailment"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer contradiction
    label = "contradiction"

print(label)
