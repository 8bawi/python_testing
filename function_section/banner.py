def banner_text(text, width):
    screen_width = width
    
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                        .format(text,screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width-4))
        print(output_string)


banner_text("*",30)
banner_text("this is line" , 3)
banner_text("*",30)