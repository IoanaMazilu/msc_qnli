# The premise gives the length of sides of a triangle STV
side_length_st = 10
side_length_tv = 10
side_length_sv = 12

# The hypothesis gives the length of sides of a triangle STV
side_length_st_hypothesis = 70
side_length_tv_hypothesis = 70
side_length_sv_hypothesis = 12

# Compute the length of sides in the hypothesis
side_length_st_hypothesis_computed = side_length_st_hypothesis / side_length_st
side_length_tv_hypothesis_computed = side_length_tv_hypothesis / side_length_tv
side_length_sv_hypothesis_computed = side_length_sv_hypothesis / side_length_sv

# Check if the length of sides in the hypothesis contradicts the length of sides in the premise
if side_length_st_hypothesis_computed!= side_length_st or side_length_tv_hypothesis_computed!= side_length_tv or side_length_sv_hypothesis_computed!= side_length_sv:
    label = "contradiction"
else:
    label = "entailment"

print(label)
