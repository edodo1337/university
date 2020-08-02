FACULTY_POSITION_CHOICES = (
    (1, "Декан"),
    (2, "Заведующий кафедрой"),
    (3, "Профессор"),
    (4, "Доцент"),
    (5, "Преподаватель"),
)

RECTORATE_POSITION_CHOICES = (
    (6, "Ректор"),
    (7, "Проректор по науке"),
    (8, "Проректор по образованию"),
    (9, "Проректор по экономике"),
)

POSITION_CHOICES = ((0, "----"),) + RECTORATE_POSITION_CHOICES + FACULTY_POSITION_CHOICES

NONE_TYPE = 0
RECTORATE_TYPE = 1
FACULTY_TYPE = 2
CHAIN_TYPE = 3

DIVISION_TYPE_CHOICES = (
    (NONE_TYPE, "----"),
    (RECTORATE_TYPE, "Ректорат"),
    (FACULTY_TYPE, "Факультет"),
    (CHAIN_TYPE, "Кафедра"),
)

FACULTY_LEAD_POSITION = 1
CHAIN_LEAD_POSITION = 2
RECTORATE_LEAD_POSITION = 6
