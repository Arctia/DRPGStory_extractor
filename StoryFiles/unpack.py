import os
import UnityPy
import json

TO_DECRYPT = ['area', 'event', 'story', 'storytalk', 'storycharacter', 'episode']

def unpack_all_assets(source_folder : str, destination_folder : str):
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            env = UnityPy.load(file_path)
            for obj in env.objects:
                if obj.type.name == "MonoBehaviour":
                    if obj.serialized_type.nodes:

                        tree = obj.read_typetree()
                        if not tree['m_Name'] in TO_DECRYPT: continue
                        
                        fp = os.path.join(destination_folder, f"{tree['m_Name']}.json")
                        with open(fp, "wt", encoding = "utf8") as f:
                            json.dump(tree, f, ensure_ascii = False, indent = 4)
                    else:
                        data = obj.read()
                        fp = os.path.join(destination_folder, f"{data.name}.bin")
                        with open(fp, "wb") as f:
                            f.write(data.raw_data)
                    if obj.serialized_type.nodes:
                        tree = obj.read_typetree()
                        obj.save_typetree(tree)
                    else:
                        data = obj.read()
                        with open(os.path.join(destination_folder, data.name)) as f:
                            data.save(raw_data = f.read())

if __name__ == '__main__':
    unpack_all_assets("./masters/", "./master_json/")