anita_days = 18
indu_days = 27
geeta_days = 36

# the hypothesis refers to the same work done by Anita, Indu and Geeta
# but with different time periods
anita_days_hyp = 58
indu_days_hyp = 27
geeta_days_hyp = 36

# the hypothesis states the same time periods for Anita, Indu and Geeta
# as stated in the premise
if anita_days_hyp!= anita_days or indu_days_hyp!= indu_days or geeta_days_hyp!= geeta_days:
    # check if the time periods in the hypothesis contradict the time periods in the premise
    label = "contradiction"
else:
    # if the time periods in the hypothesis do not contradict the time periods in the premise,
    # we can infer entailment
    label = "entailment"

print(label)
