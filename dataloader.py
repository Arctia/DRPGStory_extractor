
import os, json

class DataLoader():

	PATH = "./StoryFiles/"

	def __init__(self, jp=True):
		if jp: 
			self._init_jp()
			return
		self.story = self.load_json("Story")
		self.story_talk = self.load_json("StoryTalk")
		self.story_character = self.load_json("StoryCharacter")

		self.area = self.load_json("Area")
		self.episode = self.load_json("Episode")
		self.event = self.load_json("Event")

	def _init_jp(self):
		self.story = self.load_jp_json("story")
		self.story_talk = self.load_jp_json("storytalk")
		self.story_character = self.load_jp_json("storycharacter")

		self.area = self.load_jp_json("area")
		self.episode = self.load_jp_json("episode")
		self.event = self.load_jp_json("event")

	def load_json(self, filename):
		file_path = os.path.join(self.PATH, "EN", filename + ".json")
		with open(file_path) as f:
			arr = json.load(f)
		return (arr)

	def load_jp_json(self, filename):
		file_path = os.path.join(self.PATH, "master_json", filename + ".json")
		with open(file_path) as f:
			arr = json.load(f)["DataList"]
		return (arr)
