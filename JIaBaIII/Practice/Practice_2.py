s = "this is a string"

li_st = list(s)  # convert to list
print(li_st)
vvvvenus = li_st.index("i")
# print(vvvvenus)
del(li_st[vvvvenus])

li_st[0:2] = []  # really delete letter h (the item is actually removed from the list)  # another way to delete it

p = li_st.index("s")  # find position of the letter "s"
del(li_st[p])         # delete it

s = "".join(li_st)  # convert back to string

print(s)
