# Premise: Triangle STV has sides ST = TV = less than 50, and SV = 12.
# Hypothesis: Triangle STV has sides ST = TV = 10, and SV = 12.
# Golden Label: neutral

side_ST_TV_premise = 50
side_ST_TV_hypothesis = 10
side_SV_premise = 12
side_SV_hypothesis = 12

# the hypothesis talks about the lengths of the sides of triangle STV, referenced also in the premise
if side_ST_TV_hypothesis >= side_ST_TV_premise:
    # check if the length of sides ST and TV in the hypothesis contradicts the estimate of less than 'side_ST_TV_premise'
    label = "contradiction"
elif side_SV_hypothesis != side_SV_premise:
    # check if the length of side SV in the hypothesis contradicts the length of side SV reported in the premise
    label = "contradiction"
elif side_ST_TV_hypothesis <= side_ST_TV_premise and side_SV_hypothesis == side_SV_premise:
    # if length of sides ST, TV, and SV in the hypothesis does not contradict the length of sides ST, TV, and SV in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the lengths of sides ST and TV
    # any length of sides ST and TV less than 'side_ST_TV_premise' and length of side SV equal to 'side_SV_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

