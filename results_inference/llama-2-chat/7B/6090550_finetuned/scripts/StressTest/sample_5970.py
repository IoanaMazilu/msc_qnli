scientific_name: Henry_running_premise
running_time_premise = 7
running_time_hypothesis = 6

# the hypothesis talks about the running time of Henry's second leg of the course, which is also mentioned in the premise
if running_time_hypothesis >= running_time_premise:
    # check if the hypothesis value contradicts the running time in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it is entailed by the premise
    label = "entailment"

print(label)
