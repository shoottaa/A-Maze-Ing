WALL_COLORS = [
    0xFFFFFFFF,  # blanc (défaut)
    0xFFFF0000,  # rouge
    0xFF00FF00,  # vert
    0xFF0000FF,  # bleu
    0xFFFFFF00,  # jaune
    0xFF00FFFF,  # cyan
    0xFFFF00FF,  # magenta
]


class ColorManager:

    def __init__(self) -> None:
        """Gère la couleur des murs en fonction de WALL_COLORS"""
        self.index = 0

    def current(self) -> bytes:
        """Retourne la couleur actuelle des murs"""
        return WALL_COLORS[self.index].to_bytes(4, 'little')

    def cycle(self) -> None:
        """Change la couleur des murs en fonction de WALL_COLORS"""
        self.index = (self.index + 1) % len(WALL_COLORS)
