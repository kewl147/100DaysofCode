def format_name(f_name, l_name):
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"\n{format_f_name} {format_l_name}"

formated_string = format_name("pATRICK", "DiLlOn")

print(formated_string)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))

print(output)