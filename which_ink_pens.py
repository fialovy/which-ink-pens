# Absolutely ridiculous thing I wrote because I want my daily pens to
# dry out at the same rate.

from datetime import date

# I have a 10 pack of colored Pilot Frixion ball pens.
# You should get some if you want to enjoy this program properly.
PEN_PAIRINGS = [
    ('black', 'purple'),
    ('navy', 'pink'),
    ('blue', 'red'),
    ('light blue', 'orange'),
    ('dark green', 'light green'),
]
NORMS_BIRTHDAY = date(1992, 6, 26)

def main():
    days_since = (date.today() - NORMS_BIRTHDAY).days
    pens_index = days_since % len(PEN_PAIRINGS)
    first_color, second_color = PEN_PAIRINGS[pens_index]
    print(
        f'For optimal and even obsolesence, please use the {first_color} '
        f'pen and the {second_color} pen today.'
    )

if __name__ == '__main__':
    main()
