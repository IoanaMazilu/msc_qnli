anita_days = 18
indu_days = 27
geeta_days = 36

# hypothesis refers to the time taken by Anita, Indu and Geeta to complete a piece of work
# the hypothesis states that Anita, Indu and Geeta can complete the work in less than 38 days, 27 days and 36 days respectively
if anita_days >= 38 or indu_days >= 38 or geeta_days >= 38:
    # check if the time taken by Anita, Indu or Geeta to complete the work contradicts the hypothesis
    label = "contradiction"
elif anita_days >= 38 or indu_days >= 38 or geeta_days >= 38:
    # check if the time taken by Anita, Indu or Geeta to complete the work contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
