# define variables for the numerical entities in the premise
internacional_score_premise = 4
seongnam_ilhwa_chunma_score_premise = 2
alecsandro_scored_twice_premise = 2

# define variables for the numerical entities in the hypothesis
internacional_score_hypothesis = 4
seongnam_ilhwa_chunma_score_hypothesis = 2

# check if the hypothesis mentions the same scores as the premise
if internacional_score_hypothesis!= internacional_score_premise:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif seongnam_ilhwa_chunma_score_hypothesis!= seongnam_ilhwa_chunma_score_premise:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif alecsandro_scored_twice_premise!= 2:
    # check if the number of goals scored by Alecsandro in the hypothesis contradicts the number of goals scored by Alecsandro in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
