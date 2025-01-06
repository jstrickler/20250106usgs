from scipy import constants as K  # alias scipy.constants to save typing

print(f"pi: {K.pi}")  # some constants are built in
print(f"Planck: {K.Planck}")  # some constants are built in
print(f"c (speed of light): {K.c}")  # some constants are built in

print(f"natural unit of energy: {K.value('natural unit of energy')}")
print(f"natural unit of energy (Unit): {K.unit('natural unit of energy')}")
