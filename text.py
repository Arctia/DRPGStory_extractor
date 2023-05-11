
from dataloader import DataLoader
import json, os

def get_name(t):
	options = ['chara1_name', 'chara2_name', 'chara3_name']
	for o in options:
		if t[o] != "":
			return t[o]

def write_story(db):
	for ep in db.episode:

		ep_dir = f"{str(ep['id']).rjust(6, '0')}. {ep['name'].replace(' ', '_')}"
		if not os.path.exists(ep_dir): os.mkdir(ep_dir)
		area_num = 0
		for area in db.area:
			if area['m_episode_id'] != ep['id']: continue

			area_num += 1 
			f_name = f"0{area_num}.{area['name'].replace(' ', '_')}.txt" 
			file = open(os.path.join(ep_dir, f_name), "w")
			text = ""
			for story in db.story:
				if int(story['id'] / 10) != area['id']: continue

				text += f"[{story['title']}]\n"
				for	talk in db.story_talk:
					if talk['m_story_id'] != story['id']: continue

					name = get_name(talk)
					chat = talk['talk_text'].replace("\n", " ")
					text += f"{name}: {chat}\n"

				text += "\n"

			file.write(text)
			file.close()

		print(f"end ep: {ep['name']}")

def	write_events(db):
	for ep in db.event:
		event_types = [6] # [1, 15]
		if not ep['event_type'] in event_types: continue

		ep_dir = f"{str(ep['id']).rjust(3, '0')}. {ep['resource_name'].replace(' ', '_')}"
		if not os.path.exists(ep_dir): os.mkdir(ep_dir)

		area_num = 0
		
		for area in db.area:
			if area['m_episode_id'] != ep['m_episode_id']: continue

			area_num += 1 
			f_name = f"0{area_num}.{area['name'].replace(' ', '_')}.txt" 
			file = open(os.path.join(ep_dir, f_name), "w")
			text = ""

			for story in db.story:
				divider = 10 if ep['event_type'] == 15 else 100
				if int(story['id'] / divider) != area['id']: continue

				text += f"[{story['title']}]\n"
				for	talk in db.story_talk:
					if talk['m_story_id'] != story['id']: continue

					name = get_name(talk)
					chat = talk['talk_text'].replace("\n", " ")
					text += f"{name}: {chat}\n"

				text += "\n"

			file.write(text)
			file.close()

		print(f"Ended: {ep['resource_name']}")

def	write_raids(db):
	for ep in db.event:
		event_types = [6] # [1, 15]
		if not ep['event_type'] in event_types: continue

		ep_dir = f"{str(ep['id']).rjust(3, '0')}. {ep['resource_name'].replace(' ', '_')}"
		if not os.path.exists(ep_dir): os.mkdir(ep_dir)

		for story in db.story:
			if story['id'] != ep['prologue_story_id'] and story['id'] != ep['ending_story_id']: continue
			pro = '00.' if story['id'] == ep['prologue_story_id'] else '01.'
			f_name = f"{pro}.{story['title']}.txt"
			file = open(os.path.join(ep_dir, f_name), "w")
			text = ""
			
			for	talk in db.story_talk:
				if talk['m_story_id'] != story['id']: continue
		
				name = get_name(talk)
				chat = talk['talk_text'].replace("\n", " ")
				text += f"{name}: {chat}\n"

			text += "\n"
			file.write(text)
			file.close()

		print(f"Ended: {ep['resource_name']}")

def	main():
	db = DataLoader(jp = False)

	base_path = "Diary/"
	if not os.path.exists(base_path): os.mkdir(base_path)
	os.chdir(base_path)

	# write_story(db)
	# write_events(db)
	write_raids(db)

if __name__ == '__main__':
	main()
