class Prism:
    def __init__(self):
        self.vertices = [
            (1, 1, 0),  # Vertex 0
            (-1, 1, 0),  # Vertex 1
            (0, -1, 0),  # Vertex 2
            (1, 1, 1),  # Vertex 3
            (-1, 1, 1),  # Vertex 4
            (0, -1, 1),  # Vertex 5
        ]

        self.edges = [
            # Front Face
            (0, 1),
            (1, 2),
            (2, 0),
            # Back Face
            (3, 4),
            (4, 5),
            (5, 3),
            # Side Faces
            (0, 3),
            (1, 4),
            (2, 5)
        ]
