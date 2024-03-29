
import os, json

class DataLoader():

	PATH = "./StoryFiles/"

	def __init__(self, jp=True):
		if jp: 
			self._init_jp()
		self._init_en()

	def _init_en(self):
		self.story_en = self.load_en_json("Story")
		self.story_talk_en = self.load_en_json("StoryTalk")
		self.story_character_en = self.load_en_json("StoryCharacter")

		self.area_en = self.load_en_json("Area")
		self.episode_en = self.load_en_json("Episode")
		self.event_en = self.load_en_json("Event")

	def _init_jp(self):
		self.story = self.load_jp_json("story")
		self.story_talk = self.load_jp_json("storytalk")
		self.story_character = self.load_jp_json("storycharacter")

		self.area = self.load_jp_json("area")
		self.episode = self.load_jp_json("episode")
		self.event = self.load_jp_json("event")

	def load_en_json(self, filename):
		file_path = os.path.join(self.PATH, "EN", filename + ".json")
		with open(file_path, encoding='utf-8') as f:
			data = json.load(f)
		return (data)

	def load_jp_json(self, filename):
		file_path = os.path.join(self.PATH, "master_json", filename + ".json")
		with open(file_path, encoding='utf-8') as f:
			data = json.load(f)["DataList"]
		return (data)
