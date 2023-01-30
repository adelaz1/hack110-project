class todo:
    id: int
    title: str
    description: str
    color: str
    category: str
    fave: str
    checked: bool

    def __init__(self, id: int, title: str, description: str, color: str, category: str, fave: str):
        self.id = id
        self.title = title
        self.description = description
        self.color = color
        self.category = category
        self.fave = fave
        self.checked = False

