from pdf2image import convert_from_path

pdf_file = "Resume_Template__1_ (1).pdf"

pages = convert_from_path(pdf_file)

pages[0].save(
    "resume.gif",
    save_all=True,
    append_images=pages[1:],
    duration=1000,
    loop=0
)

print("GIF ban gayi!")