speed_f_premise = 8
speed_s_premise = 5
speed_f_hypothesis = 5
speed_s_hypothesis = 5

# the hypothesis refers to the speeds of Fred and Sam mentioned in the premise
if speed_f_hypothesis!= speed_f_premise or speed_s_hypothesis!= speed_s_premise:
    # check if the speeds in the hypothesis contradict the speeds in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speeds
    # any combination of speeds consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
