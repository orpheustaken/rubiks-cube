from abc import ABC, abstractmethod

# Cube Abstract Class.
# TODO: Apply static typing annotations.
class Cube(ABC):
    # Neighbor Pieces?
    # Parallel impacts?
    def __init__(self, og_centre_face, piece_position, coordinates):
        self.og_centre_face =  og_centre_face
        self.piece_position = piece_position
        self.coordinates = coordinates

    @abstractmethod
    def move_piece():
        pass
