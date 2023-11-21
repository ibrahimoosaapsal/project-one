def common_letters():
    str1=input("enter first string :-")
    str2=input("enter second string :-")
    s1=set(str1)
    s2=set(str2)
    list=s1&s2
    print(list)


common_letters()