tin_industry_premise = "Indonesia's tin industry"
tin_mine_premise = "Tambang Timah"
cost_cut_premise = 25

tin_industry_hypothesis = "Indonesia"
cost_cut_hypothesis = 25

# the hypothesis talks about the cost cut of the tin industry in Indonesia, which is also mentioned in the premise
if cost_cut_hypothesis!= cost_cut_premise:
    # check if the cost cut in the hypothesis contradicts the cost cut from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
