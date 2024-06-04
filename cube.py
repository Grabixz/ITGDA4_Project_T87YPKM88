class Cube:
    def __init__(self):
        self.vertices = [
            (1, -1, -1),  # Vertex 0
            (1, 1, -1),  # Vertex 1
            (-1, 1, -1),  # Vertex 2
            (-1, -1, -1),  # Vertex 3
            (1, -1, 1),  # Vertex 4
            (1, 1, 1),  # Vertex 5
            (-1, -1, 1),  # Vertex 6
            (-1, 1, 1)  # Vertex 7
        ]

        self.edges = [
            # Front Face
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            # Back Face
            (4, 5),
            (5, 7),
            (7, 6),
            (6, 4),
            # Side Faces
            (0, 4),
            (1, 5),
            (2, 7),
            (3, 6)
        ]
