# Premise: For sailors, the lighthouse of Alexandria ensured a safe return to the Great Harbor ; for architects, it was the tallest building on Earth ; and for scientists, it was the mysterious mirror that fascinated them most:its reflection could be seen more than 50 km (35 miles) off-shore. For all these reasons, the lighthouse was considered one of the Seven Wonders of the world.
# Hypothesis: The lighthouse of Alexandria was one of the seven wonders of the world.
# Golden Label: entailment

wonders_premise = 7
wonders_hypothesis = 7

# the hypothesis talks about the lighthouse of Alexandria being one of the seven wonders, which is also mentioned in the premise
if wonders_hypothesis != wonders_premise:
    # check if the number of wonders in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

