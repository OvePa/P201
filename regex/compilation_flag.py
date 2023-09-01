import re


def validate_input(input_email):
    re_compilation = re.compile(
        r"""
                           ^([a-z0-9_\.-]+)      #it will pick the first local part
                           @                     # will pick the @ sign
                            ([0-9a-z\.-]+)       # will pick the domain name
                           \.                    # will have single "."
                            ([a-z]{2,6})$        # it will pick the top level Domain (last part)    
                           """,
        re.VERBOSE,
    )

    result = re_compilation.fullmatch(input_email)

    if result:
        print("{} is Valid.".format(input_email))

    else:
        print("{} is Invalid".format(input_email))


validate_input("name@gmail.com")
validate_input("educative@.com")
