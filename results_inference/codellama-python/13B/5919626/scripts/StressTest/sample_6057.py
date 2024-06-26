days_anita_premise = 18
days_indu_premise = 27
days_geeta_premise = 36
days_anita_hypothesis = 38
days_indu_hypothesis = 27
days_geeta_hypothesis = 36

# the hypothesis talks about the number of days needed to do a piece of work
# the premise gives estimates for the number of days needed to do a piece of work
if days_anita_hypothesis <= days_anita_premise:
    # check if the hypothesis value contradicts the estimate of less than 'days_anita_premise'
    label = "contradiction"
elif days_indu_hypothesis!= days_indu_premise:
    # check if the number of days needed to do a piece of work in the hypothesis contradicts the number of days needed to do a piece of work in the premise
    label = "contradiction"
elif days_geeta_hypothesis!= days_geeta_premise:
    # check if the number of days needed to do a piece of work in the hypothesis contradicts the number of days needed to do a piece of work in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
