from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Guest(ABC):
    number_guest: int

