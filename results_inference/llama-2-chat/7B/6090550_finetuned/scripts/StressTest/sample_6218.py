yt_entailment = 0
yt_contradiction = 0
yt_neutral = 1

# the hypothesis talks about the number of stations between Delhi and Chennai, which is also mentioned in the premise
if hypothesis_stations > premise_stations:
    # check if the number of stations in the hypothesis contradicts the number of stations in the premise
    yt_contradiction = 1
elif hypothesis_stations < premise_stations:
    # check if the number of stations in the hypothesis is less than the number of stations in the premise
    yt_contradiction = 1
else:
    # if the number of stations in the hypothesis does not contradict the number of stations in the premise, we can infer entailment
    yt_entailment = 1

print(yt_entailment)
print(yt_contradiction)


