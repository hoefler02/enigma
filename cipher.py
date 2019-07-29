#!/usr/bin/env python3

from enigma import *

rf = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')

r1 = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 13, 3)
r2 = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 10, 9)
r3 = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 24, 5)

machine = EnigmaMachine([r1, r2, r3], rf)

message = 'JFMKWTXUUQ'

print(machine.decrypt(message))