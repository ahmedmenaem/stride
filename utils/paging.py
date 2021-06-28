def get_pagination(page):
    entities_number = 10
    page = int(page)
    try:
        if page and page > 0:
            limit = entities_number
            offset = page * entities_number - entities_number;
            return limit, offset, page
        else:
            return entities_number, 0, 1
    except:
        return entities_number, 0, 1