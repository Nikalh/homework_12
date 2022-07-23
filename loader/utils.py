# функция для записи картинок(изображений)
def save_picture(picture)->str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path