# The premise gives the length of the sides of the triangle STV
side_length_premise = 50

# The hypothesis gives the length of the sides of the triangle STV
side_length_hypothesis = 10

# The premise does not mention the length of the SV side
sv_side_length_premise = 12

# The hypothesis mentions the length of the SV side
sv_side_length_hypothesis = 12

# The premise and hypothesis both mention the length of the ST side
st_side_length_premise = 50
st_side_length_hypothesis = 10

# The premise and hypothesis contradict each other in the length of the ST side
if st_side_length_premise!= st_side_length_hypothesis:
    label = "contradiction"
elif side_length_premise < side_length_hypothesis:
    label = "entailment"
else:
    label = "neutral"

print(label)
