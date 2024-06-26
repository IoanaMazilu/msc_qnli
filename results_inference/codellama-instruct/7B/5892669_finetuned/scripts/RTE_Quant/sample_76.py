demonstration_premise = 25
counter_demonstration_premise = 25
demonstration_hypothesis = 25
counter_demonstration_hypothesis = 25

# the hypothesis talks about the number of Palestinian and Israeli demonstrations, which are also mentioned in the premise
if demonstration_hypothesis!= demonstration_premise:
    # check if the number of Palestinian demonstrations in the hypothesis contradicts the number of Palestinian demonstrations from the premise
    label = "contradiction"
elif counter_demonstration_hypothesis!= counter_demonstration_premise:
    # check if the number of counter-demonstrations in the hypothesis contradicts the number of counter-demonstrations in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
