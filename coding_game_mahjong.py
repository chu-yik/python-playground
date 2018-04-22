# this is my solution to coding game community puzzle
# https://www.codingame.com/training/community/completed-mahjong-hands?utm_term=en&utm_source=Digest&utm_medium=puzzle_week&utm_content=view&utm_campaign=Notifications

import time

def is_kokushi_musou(hand):
	required = {'m1', 'm9', 'p1', 'p9', 's1', 's9', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7'}
	return set(hand) == required

def is_seven_pairs(hand):
	set_hand = set(hand)
	if len(set_hand) == 7:
		for item in set_hand:
			if hand.count(item) != 2:
				return False
		return True
	else:
		return False

# forming run is a bit hacky there
# t_count == p1_count is just too hacky.. damn
def form_run(hand):
	runs = []
	temp = hand.copy()
	for tile in temp:
		# check if a run can be formed
		prefix = tile[0]
		if prefix in ('m', 'p', 's'):
			suffix = int(tile[1])
			if suffix < 8:
				plus_one = '{}{}'.format(prefix, suffix+1)
				plus_two = '{}{}'.format(prefix, suffix+2)
				t_count = hand.count(tile)
				p1_count = hand.count(plus_one)
				p2_count = hand.count(plus_two)
				if t_count > 0 and p1_count > 0 and p2_count > 0 and t_count == p1_count:
					hand.remove(tile)
					hand.remove(plus_one)
					hand.remove(plus_two)
					runs.append([tile, plus_one, plus_two])
	return runs

def form_triplet(hand):
	triplets = []
	temp = hand.copy()
	for tile in temp:
		if hand.count(tile) >= 3:
			hand.remove(tile)
			hand.remove(tile)
			hand.remove(tile)
			triplets.append(tile)
	return triplets

def check_winning(hand):
	triplets = form_triplet(hand)
	triplet_count = len(triplets)
	# m p s can be triplet or run 
	runs = form_run(hand)
	run_count = len(runs)

	if triplet_count + run_count == 4 and len(set(hand)) == 1:
		return True
	
	# print('triplets {}, runs {}, hand {}'.format(triplets, runs, hand))
	
	if len(hand) > 2:
		return False

	if hand[0][0] != hand[1][0]:
		return False

	prefix = hand[0][0]
	# z can only for triplet
	if prefix == 'z':
		return False

	start = int(hand[0][1])
	end = int(hand[1][1])

	# if what we have is like p3 p4, then we see if p2 and p5 are in triplets
	# if what we have is like p5 p7, then we see if p6 is in triplets
	if end - start == 1:
		target1 = '{}{}'.format(prefix, start-1)
		target2 = '{}{}'.format(prefix, end+1)
		return triplets.count(target1) > 0 or triplets.count(target2) > 0
	elif end - start == 2:
		target = '{}{}'.format(prefix, start+1)
		return triplets.count(target) > 0
	else:
		return False

def check_complete_hand(line):
	hand = []
	# parse line into hand
	for c in reversed(line.lower().replace(' ', '')):
		if c in ('m', 'p', 's', 'z'):
			prefix = c
		else:
			hand.append('{0}{1}'.format(prefix, c))
	hand.sort()

	# if is_kokushi_musou(hand):
	# 	print('{} is kokushi'.format(line))
	# elif is_seven_pairs(hand):
	# 	print('{} is seven pairs'.format(line))
	# elif check_winning(hand):
	# 	print('{} is a win'.format(line))
	
	if is_kokushi_musou(hand) or is_seven_pairs(hand) or check_winning(hand):
		print('TRUE')
	else:
		print('FALSE')

start_time = time.time()

check_complete_hand('222888m444p2277z 7z') # true
check_complete_hand('19m19p19s1234567z 6z') # true - kokushi
check_complete_hand('11m4477p8899s116z 6z') # true - 7 pair
check_complete_hand('122223567m3555p 4p') # true
check_complete_hand('1122223m111222z 4m') # true - complicated
check_complete_hand('19m139p19s123567z 4z') # false - not kokushi
check_complete_hand('11m4477p8899s666z 6z') # false - not 7 pairs
check_complete_hand('1122335778899m 1m') # false - not 7 pairs
check_complete_hand('234m45789p45688s 6p') # true
check_complete_hand('1133344566777m 9m') # false - not 7 pairs
check_complete_hand('1133344566777m 5m') # true
check_complete_hand('123345567789m3p 3p') # true

print("time used = %s seconds" % (time.time() - start_time))