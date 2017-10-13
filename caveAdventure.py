#The goal to this game is to escape the cave!
import time

def intro():
	print("""
			You wake up in an unfamiliar place. Your head hurts, you can't quite see
			straight. You hear the distant sound of water dripping. The ground is very
			hard and you're surrounded by rocks. You somehow got lost in a cave! You
			have no idea what could be lurking in here, so you gotta outta here, fast!
				""")
	cave_main()

def cave_main():
	print("""
			What do you want to do?

			Press R then enter to Rest for a minute
			Press L then enter to Look around
			Press S then enter to Sleep
			  """)
	choice = input()

	if choice == 'r':
		print("""
			You chose to rest. As you sit for a minute and compose yourself, your headache goes
			away, and your eyesight returns to normal. Now that you can think straight again,
			you start to make a plan to escape.
			    """)
		rested()
	elif choice == 'l':
		print("""
			You try to look around, but you're too disoriented and in too much pain.
			Perhaps you should rest for a bit.
				""")
		time.sleep(3)
		cave_main()
	elif choice == 's':
		print("""
			You chose to sleep. While you sleep, a bear discovers your body and decides to
			have a little snack. You wake up just in time to feel the bear bite into your skull
			before you hear a loud ~CRACK~ and everything goes dark.
				""")
		time.sleep(5)
		print("""
			Game over!
				  """)
		quit

def rested():
	print("""
			You are in the main part of the cave.

			Press L to Look around
			Press Y to Yell for help
			  """)
	choice = input()
	if choice == 'l':
		look_around()
	elif choice == 'y':
		print("""
			You yell for help, and all you hear is the faint echo of your cries. No one can
			help you. You need to save yourself.
        """)
		time.sleep(3)
		rested()

def look_around():
	print("""
			When you look around, you notice there are several paths leading 
			away from the area. One path leading towards the sound of dripping
			water, another leading into a very dark area, and a small hole that
			looks like you can crawl through.

			Press W to go towards the Water
			Press C to Crawl through the hole
			Press D to check the Dark area
			  """)
	choice = input()
	if choice == 'w':		
		water()
	elif choice == 'c':
		crawl()
	elif choice == 'd':
		dark()

def water():
	print("""
			As you make your way towards the sound of water, you begin to see a source
			of light. You then see lit a torch lying on the ground. This could help
			you explore the cave.

			Press T to Take the torch
			Press R Return to the cave
				""")
	choice = input()
	if choice == 't':
		hasTorch = True	
		print("""
			You have taken the torch, and you can see much better now.
				""")
		time.sleep(2)
		cave_torch()
	elif choice == 'r':
		hasTorch = False	
		rested()

def crawl():
	print("""
			You barely manage to crawl through the hole. You come out the other side,
			and see a faint beam of light poking through the rocks. When you look closer,
			you can see outside the cave! The rocks are way too heavy and compacted to 
			move by hand. If you had some kind of tool, then you might be able to escape!

			Press R to Return to the cave
				""")
	choice = input()
	if choice == 'r':
		rested()

def dark():
	print("""
			You step into the dark area, but you can't see a thing. You need a way to 
			light the path.
				""")
	time.sleep(3)
	look_around()

def cave_torch():	
	print("""
			You are now in the cave with the torch.

			Press W to go towards the Water
			Press D to check the Dark area
			Press C to Crawl through the hole
				""")
	choice = input()
	if choice == 'w':
		print("""
			There is nothing else here.
						""")
		time.sleep(3)
		cave_torch()		
	if choice == 'd':
		print("""
			As you enter the area, you see an object shining on the ground. Upon
			inspection, you realize it's a pickaxe! This might come in handy.

			Press P to Pickup the axe
			Press R to Return to the cave
			  """)
		choice = input()
		if choice == 'p':
			print("""
			You have taken the pickaxe.
				  """)
			cave_final()
		elif choice == 'r':
			cave_torch()
	elif choice == 'c':
		crawl()

def cave_final():
	print("""
			Now you should have everything you need to escape!

			Press W to go towards the Water
			Press D to go to the Dark Area	
			Press C to Crawl through the hole
          """)
	choice = input()
	if choice == 'w':
		print("""
			There is nothing else here.
						""")
		time.sleep(3)
	elif choice == 'd':
		print("""
			There is nothing else here.
						""")
		time.sleep(3)
		cave_final()
	if choice == 'c':
  		escape()

def escape():
	print("""
			You crawl through the hole again. Armed with the pickaxe, you should be able to
			move the rocks out of the way.

			Press P to use Pickaxe
				""")
	choice = input()
	if choice == 'p':
		print("""
			You use the pickaxe to pull the rocks out of the way. They are extremely heavy and
			hard to move, but you manage to move them. The pickaxe is weakening, only a couple
			more rocks to go. You give it one last whack. The rocks fall out of the way as the pickaxe 
			breaks apart. You can now make your escape!
					""")

	time.sleep(6)
	
	print("""
			Congratulations! You escaped!

			Play again? (y/n)
				""")
	choice = input()
	if choice == 'y':
		intro()
	elif choice == 'n':
			quit

intro()