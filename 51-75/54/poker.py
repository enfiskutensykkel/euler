#!/usr/bin/env python

value = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class card(object):
	def __init__(self, card):
		self.value = value[card[0]] if card[0] in value else int(card[0])
		self.suit = card[1]

	def __repr__(self):
		return str(self.value) + self.suit

	def __cmp__(self, other):
		return cmp(self.value, other.value)

class hand(object):
	def __init__(self, cards):
		self.cards = sorted(cards)

	def N_of_a_kind(self):
		kinds = []
		found = {}

		for N in xrange(4, 1, -1):

			for i in xrange(len(self.cards) - N):
				fcards = self.cards[i:i+N]
				rcards = self.cards[::-1][i:i+N]

				for cards in fcards, rcards:
					v = cards[0]
					if v.value in found and found[v.value] <= i:
						continue

					contains = True
					for card in cards[1:]:
						if not card.value == v.value:
							contains = False
							break

					if contains:
						found[v.value] = i
						kinds.append(tuple(cards))

		return kinds

	def royal_flush(self):
		return 10000 * (self.straight_flush() and self.cards[-1].value == value['A'])

	def straight_flush(self):
		return 8000 * (self.flush() and self.straight())

	def four(self):
		kinds = self.N_of_a_kind()
		for kind in kinds:
			if len(kind) == 4:
				return 7000 + kind[0].value

		return 0

	def full_house(self):
		n = self.three()
		m = self.pair()

		if n > 0 and m > 0:
			return n + m + 1000

		return 0

	def flush(self):
		suit = self.cards[0].suit
		for card in self.cards:
			if not card.suit == suit:
				return 0

		return 750 + self.cards[-1].value

	def straight(self):
		for i in xrange(4):
			if self.cards[i].value != self.cards[i + 1].value - 1:
				return 0

		return 700

	def three(self):
		kinds = self.N_of_a_kind()
		for kind in kinds:
			if len(kind) == 3:
				return 400 + kind[0].value

		return 0

	def pair(self):
		score = 0
		kinds = self.N_of_a_kind()
		second = 0
		for kind in kinds:
			if len(kind) == 2:
				score += 100 + kind[0].value + second * 50
				second += 1

		return score

	def __repr__(self):
		return " ".join([repr(card) for card in self.cards])

	def score(self):
		#score = self.cards[-1].value
		score = 0
		score += self.pair()
		score += self.three()
		score += self.straight()
		score += self.flush()
		score += self.full_house()
		#score += self.four()
		#score += self.straight_flush()
		#score += self.royal_flush()

		return score

if __name__ == '__main__':
	import re
	from urllib2 import urlopen

	P1_wins = 0
	P2_wins = 0
	wrong = 0

	#for line in open("poker.txt").readlines():
	for line in urlopen("http://projecteuler.net/project/poker.txt").readlines():
		cards = []
		for g in re.findall(r'([2-9TJQKA]{1,2}[HDCS])', line):
			cards.append(card(g))

		P1 = hand(cards[:5])
		P2 = hand(cards[5:])

		P1_score = P1.score()
		P2_score = P2.score()

		P1_wins += P1_score > P2_score
		P2_wins += P2_score > P1_score

		if P1_score == P2_score:
			for i in xrange(4, -1, -1):
				if P1.cards[i].value > P2.cards[i].value:
					P1_wins += 1
					break
				elif P2.cards[i].value > P1.cards[i].value:
					P2_wins += 1
					break

	print ""
	print P1_wins, P2_wins, (P1_wins + P2_wins), wrong
