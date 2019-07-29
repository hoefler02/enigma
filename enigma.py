#!/usr/bin/env python3

'''

Michael Hoefler

July, 2019

ENIGMA MACHINE IN PYTHON

R1 : EKMFLGDQVZNTOWYHXUSPAIBRCJ
R2 : AJDKSIRUXBLHWTMCQGZNPYFVOE
R3 : BDFHJLCPRTXVZNYEIWGAKMUSQO

UKW-A : EJMZALYXVBWFCRQUONTSPIKHGD

'''


class EnigmaMachine:
	
	ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	def __init__(self, rotors, reflector, plugboard = None):
		
		self.rotors = rotors
		self.reflector = reflector
		
		self.plugboard = plugboard if plugboard else PlugBoard('')

	def encrypt(self, plaintext):
		
		ciphertext = ''
		count = 0
		
		for character in plaintext:
			cipher_character = character
			
			for rotor in self.rotors:
				cipher_character = rotor.encrypt_character(cipher_character)
			
			cipher_character = self.reflector.reflect_character(cipher_character)
			
			for rotor in reversed(self.rotors):
				cipher_character = rotor.decrypt_character(cipher_character)
			
			ciphertext += cipher_character
			count += 1
			
			self.rotors[0].rotate()
			
			if count % 26 == 0:
				self.rotors[1].rotate()
			
			if count % pow(26, 2) == 0:
				self.rotors[2].rotate()

			# fix if len(rotors) != 3
		
		#print(self.ALPHABET[self.rotors[0].position-1],self.ALPHABET[self.rotors[1].position-1],self.ALPHABET[self.rotors[2].position-1])
		
		return ciphertext

	def decrypt(self, ciphertext):
		
		plaintext = ''
		
		count = 0
		
		for character in ciphertext:
			
			plain_character = character
			
			for rotor in self.rotors:
				
				plain_character = rotor.encrypt_character(plain_character)
			
			plain_character = self.reflector.reflect_character(plain_character)
				
			for rotor in reversed(self.rotors):
				
				plain_character = rotor.decrypt_character(plain_character)
			
			plaintext += plain_character
			
			count += 1
			
			self.rotors[0].rotate()
			
			if count % 26 == 0:
				self.rotors[1].rotate()
			
			if count % pow(26, 2) == 0:
				self.rotors[2].rotate()
		
		#print(self.ALPHABET[self.rotors[0].position-1],self.ALPHABET[self.rotors[1].position-1],self.ALPHABET[self.rotors[2].position-1])
		
		return plaintext

	def reset(self):
		pass

class Rotor:

	def __init__(self, mapping, position = 1, ringstellung = 1):
		
		assert(position > 0 and ringstellung > 0 and len(mapping) == 26)

		self.start = position
		self.position = self.start
		self.rotations = 0

		self.wiremap = dict (
			zip (
				EnigmaMachine.ALPHABET,
				mapping[26-(ringstellung-1):] + mapping[:26-(ringstellung-1)]
			)
		)
		
		self.ring_setting = ringstellung

		self.rotate(self.start)


	def rotate(self, times = 1):

		self.rotations += times
		
		mapping = ''.join (
			self.wiremap.values()
		)

		self.wiremap = dict (
			zip (
				EnigmaMachine.ALPHABET,
				mapping[times:] + mapping[:times]
			)
		)

		self.position = self.rotations % 26

		return self.position

	def encrypt_character(self, c):

		return self.wiremap[c]

	def decrypt_character(self, c):

		revmap = {
			v:k for k,v in self.wiremap.items()
		}

		return revmap[c]
	
	def set(position, ringstellung = 1):
		
		assert(position > 0 and ringstellung > 0 and len(mapping) == 26)

		self.position = self.start
		self.rotations = 0

		self.wiremap = dict (
			zip (
				EnigmaMachine.ALPHABET,
				mapping[26-(ringstellung-1):] + mapping[:26-(ringstellung-1)]
			)
		)
		
		self.ring_setting = ringstellung

		self.rotate(self.start)
		
		
	
class Reflector:

	def __init__(self, mapping):
		
		assert(len(mapping) == 26)
		
		self.wiremap = dict (
			zip (
				EnigmaMachine.ALPHABET,
				mapping
			)
		)
		
		# todo : assert one-to-one char relationships

	def reflect_character(self, c):
		
		return self.wiremap[c]

class PlugBoard:

	def __init__(self, connections):
		pass

	def translate_character(self):
		pass


