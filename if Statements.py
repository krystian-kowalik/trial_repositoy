
is_boy = True
is_tall = False

if is_boy and is_tall:
    print("You are a tall boy.")
elif is_boy and not (is_tall):
    print("You are a short boy")
elif not(is_boy) and is_tall:
    print("You aren't a boy but are tall")
else:
    print("You are either not boy or not tall or both.")