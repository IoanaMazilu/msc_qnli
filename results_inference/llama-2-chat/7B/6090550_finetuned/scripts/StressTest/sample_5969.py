y = 68

# the hypothesis talks about the time Dawson took to run the first leg of the course, which is also mentioned in the premise

# compute the time taken in the premise
time_premise = 38

# compute the time taken in the hypothesis
time_hypothesis = 68

if time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)


