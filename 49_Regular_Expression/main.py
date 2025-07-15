import re
pattern = r"[A-Z]arcelona"
text = """
Futbol Club Barcelona (Catalan pronunciation: [fudˈbɔl ˈklub bəɾsəˈlonə] ⓘ), commonly known as FC Barcelona and colloquially as Barça ([ˈbaɾsə]), is a professional football club based in Barcelona, Catalonia, Spain, that competes in La Liga, the top flight of Spanish football.

Founded in 1899 by a group of Swiss, Catalan, German, and English footballers led by Joan Gamper, the club has become a symbol of Catalan culture and Catalanism, hence the motto "Més que un club" ("More than a club").[2] Unlike many other football clubs, the supporters own and operate Barcelona. It is the third-most valuable football club in the world, worth $5.6 billion, and the world's fourth richest football club in terms of revenue, with an annual turnover of €800.1 million.[3][4] The official Barcelona anthem is the "Cant del Barça", written by Jaume Picas and Josep Maria Espinàs.[5] Barcelona traditionally play in dark shades of blue and garnet stripes, hence nicknamed Blaugrana."""

matches = re.finditer(pattern,text)

for match in matches:
    print(match)
    print(match.span())
    print(type(match.span()))

