import pdf2image


if __name__ == "__main__":
    path='./Samples/Angry_Birds.pdf'
    images = pdf2image.convert_from_path(path)

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')