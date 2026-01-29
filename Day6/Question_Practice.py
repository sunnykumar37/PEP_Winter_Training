from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: str
    enrollment: str


@dataclass
class Interview(Student):
    resume: int
    technical: int
    gd: int

    def average_score(self):
        return (self.resume + self.technical + self.gd) / 3


@dataclass
class Marks(Interview):
    start: int
    mid: int
    end: float = 0.0

    def __post_init__(self):
        self.end = self.average_score()

m = Marks(
    name="Sunny",
    roll_no="101",
    enrollment="ENR2026",
    resume=80,
    technical=70,
    gd=90,
    start=60,
    mid=75
)

print(m)

