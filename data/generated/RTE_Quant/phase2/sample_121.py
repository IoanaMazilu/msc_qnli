# Premise: ASCAP is a membership association of more than 200,000 U.S. composers, songwriters, lyricists and music publishers of every kind of music.
# Hypothesis: More than 200,000 U.S. composers, songwriters, lyricists and music publishers are members of ASCAP.
# Golden Label: entailment

members_premise = 200000
members_hypothesis = 200000

# the hypothesis talks about the number of members in ASCAP, which is also mentioned in the premise
# check if the number of members in the hypothesis contradicts the number of members from the premise
if members_hypothesis != members_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

