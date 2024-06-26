yolanda_speed = 3
bob_speed = 4

hypothesis_yolanda_speed = 5
hypothesis_bob_speed = 4

# the hypothesis refers to Yolanda's and Bob's walking rates, which are also mentioned in the premise
if yolanda_speed!= hypothesis_yolanda_speed or bob_speed!= hypothesis_bob_speed:
    # check if the walking rates in the hypothesis contradict the ones in the premise
    label = "contradiction"
else:
    # if the walking rates in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
