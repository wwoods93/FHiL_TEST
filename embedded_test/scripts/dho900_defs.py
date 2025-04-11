from dataclasses import dataclass


@dataclass
class scope_id_t:
    NAME: str
    ID: int

@dataclass
class channel_id_t:
    NAME: str
    ID: int


DHO914  = scope_id_t(NAME = "dho914",    ID = 0x00)
DHO914S = scope_id_t(NAME = "dho914s",   ID = 0x01)
DHO924  = scope_id_t(NAME = "dho924",    ID = 0x02)
DHO924S = scope_id_t(NAME = "dho924s",   ID = 0x03)