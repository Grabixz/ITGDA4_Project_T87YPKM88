class Pyramid:
    def __init__(self):
        self.vertices = [
            (0, 1, 0),  # Vertex 0
            (-1, -1, 1),  # Vertex 1
            (1, -1, 1),  # Vertex 2
            (1, -1, -1),  # Vertex 3
            (-1, -1, -1)  # Vertex 4
        ]

        self.edges = [
            # Tip of Pyramid going to base
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            # Bottom Face of Pyramid
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 1)
        ]
