COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4",
                "azure1": "#f0ffff", "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000",
                "BlanchedAlmond": "#ffebcd", "blue1": "#0000ff", "BlueViolet": "#8a2be2"}

colour_name = input("Enter colour name: ")

print("The hexadecimal code for {} is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
