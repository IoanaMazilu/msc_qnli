work_time_premise = 12
work_time_hypothesis = 32

# the hypothesis discusses the time Sakshi takes to do a piece of work, which is also mentioned in the premise
if work_time_hypothesis < work_time_premise:
    # check if the hypothesis value contradicts the time taken by Sakshi in the premise
    label = "contradiction"
elif work_time_hypothesis == work_time_premise:
    # if the time taken by Sakshi in the hypothesis is equal to the time taken in the premise, it's an entailment
    label = "entailment"
else:
    # if the time taken by Sakshi in the hypothesis is more than the time taken in the premise, it does not contradict but also cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
