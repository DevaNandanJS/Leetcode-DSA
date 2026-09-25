s= "abcddcba"
rev= ""

for ch in s:
    rev= ch+rev
if rev== s:
    print("palin")
else:
    print("mopt")