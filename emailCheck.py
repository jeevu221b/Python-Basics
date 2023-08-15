def emailChecker():
    count = 0
    while True:
        count = 0
        track = " "
        email = input("Enter your email : ")
        # rule 1
        if "@" not in email:
            continue

        # rule 2
        if "." not in email:
            continue
        for z in range(len(email)):
            if email[z] == "@":
                count += 1
                track = z
        if count > 1:
            continue

        if email[track + 1] == ".":
            continue

        if email[len(email) - 1] == ".":
            continue

        return email

        # for z in range(len(email)):
        #     if email[z] == "@":
        #         count += 1
        #         track = z
        #         # print("Inside loop")
        # # print(track)
        # # print(count)

        # if "@" in email and "." in email:
        #     if count <= 1:
        #         if email[track + 1] != ".":
        #             break


# email = "ajdhdhjd.com"
# if "@" in email or "." in email:
#     print("working")
