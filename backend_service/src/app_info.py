from typing import List
from dataclasses import dataclass, field, asdict


@dataclass(frozen=True)
class AppInfo:
    title: str = "Factored: News Analysis"
    description: str = "This is an app for Factored Datathon 2024"
    version: str = "0.0.0"
    author: str = "SaNiMa"
    credits: List[str] = field(default_factory=lambda: [
        "Sara Cardona Carrillo", 
        "Nicolás Molina Cerón", 
        "Mateo Velásquez Molina"
    ])
    repository_url: str = "https://github.com/scardonac/factored-datathon-2024-sanima"
    documentation_url: str = ""
    support_email: str = ""

    def to_dict(self) -> dict:
        return asdict(self)