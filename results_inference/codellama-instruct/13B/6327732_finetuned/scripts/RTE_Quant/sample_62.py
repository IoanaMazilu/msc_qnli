premise = "For sailors, the lighthouse of Alexandria ensured a safe return to the Great Harbor ; for architects, it was the tallest building on Earth ; and for scientists, it was the mysterious mirror that fascinated them most:its reflection could be seen more than 50 km (35 miles) off-shore. For all these reasons, the lighthouse was considered one of the Seven Wonders of the world."
hypothesis = "The lighthouse of Alexandria was one of the seven wonders of the world."

# extract the number of reasons mentioned in the premise
reasons_premise = premise.count("reason")

# extract the number of reasons mentioned in the hypothesis
reasons_hypothesis = hypothesis.count("reason")

# check if the number of reasons in the hypothesis contradicts the number of reasons in the premise
if reasons_hypothesis!= reasons_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
