from dataclasses import dataclass


@dataclass
class scope_id_t:
    NAME: str
    ID: int

@dataclass
class channel_id_t:


DHO914  = scope_id_t(NAME = "dho914",    ID = 0x00)
DHO914S = scope_id_t(NAME = "dho914s",   ID = 0x01)
DHO924  = scope_id_t(NAME = "dho924",    ID = 0x02)
DHO924S = scope_id_t(NAME = "dho924s",   ID = 0x03)





p rint(DHO914.NAME)
print ('\n')



# print(Color.RED)  # Output: Color.RED
# print(Color.RED.name)  # Output: "RED" (Name of the member)
# print(Color.RED.value)  # Output: 1 (Value of the member)