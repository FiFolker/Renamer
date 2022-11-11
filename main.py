import os
import shutil
import json

PATH_DICT = 'path_directory.json'

def fill_path_directory():
	with open(PATH_DICT, 'r') as file:
		return json.load(file)


def show_files():
	for path in path_directory:
		print(f"	=> {path} : {path_directory[path]}")


def menu_rename():
	menu = input("Menu pour renommer les fichiers :"
				 "\n	1 : Renommer tous les fichiers avec le nom du répertoire"
				 "\n	2 : Renommer un à un"
				 "\n	3 : Renommer tous les fichiers avec un nom spécifique"
				 "\n>>")

	show_files()
	rename_file(int(menu))


def rename_file(option=1):
	answer = input("Dans quel dossier voulez vous modifier les noms ?\n>>")
	if option == 1:
		i = 0
		for files in os.listdir(path_directory[answer]):
			file_split = os.path.splitext(files)
			dirname = os.path.basename(path_directory[answer])
			print("before : " + files)
			os.rename(os.path.join(path_directory[answer], files),
					  os.path.join(path_directory[answer], dirname + ' ' + str(i) + file_split[1]))
			print("after : " + dirname + ' ' + str(i) + file_split[1])
			i += 1
	elif option == 2:
		for files in os.listdir(path_directory[answer]):
			file_split = os.path.splitext(files)
			print("before : " + files)
			new_name = input("Quel nouveau nom voulez vous lui donner ?\n>>")
			os.rename(os.path.join(path_directory[answer], files),
					  os.path.join(path_directory[answer], new_name + file_split[1]))
			print("after : " + new_name + file_split[1])
	elif option == 3:
		i = 0
		new_name = input("Quel nouveau nom voulez vous leur donner ?\n>>")
		for files in os.listdir(path_directory[answer]):
			file_split = os.path.splitext(files)
			print("before : " + files)
			os.rename(os.path.join(path_directory[answer], files),
					  os.path.join(path_directory[answer], new_name + ' ' + str(i) + file_split[1]))
			print("after : " + file_split[0] + file_split[1])
			i += 1


def rename_extension():
	answer = input("Dans quel dossier voulez vous modifier les noms ?\n>>")
	extensions = input("Quelle est la nouvelle extension que vous voulez définir ?\n>>")
	for files in os.listdir(path_directory[answer]):
		file_split = os.path.splitext(files)
		print("before : " + files)
		os.rename(os.path.join(path_directory[answer], files),
				  os.path.join(path_directory[answer], file_split[0] + "." + extensions))
		print("after : " + file_split[0] + file_split[1])

def delete_folder_in_directory():
	choice = input("Que voulez vous faire :"
				   "\n		1 : Retirer le répertoire du dictionnaire directory"
				   "\n		2 : Le supprimer définitivement du PC (avec ses fichiers) et du dictionnaire directory\n>>")
	if choice == "1":
		key = input("Quel est le répertoire que vous voulez retirer ? (donnez sa clé)\n>>")
		print(f"{path_directory[key]} à bien été retiré du dictionnaire")
		del path_directory[key]
		with open(PATH_DICT, 'w') as fw:
			json.dump(path_directory, fw, indent=4, sort_keys=True)
	elif choice == "2":
		answer = input("Quel est le répertoire que vous voulez supprimer ? (donnez sa clé)\n>>")
		print(f"Suppression de {path_directory[answer]}.")
		shutil.rmtree(path_directory[answer])
		print("Suppression terminé avec succès.")


def add_path_to_directory():
	key = input("Quel clé voulez vous lui attribuer ? (nom court de préférence)\n>>")
	path = input("Donnez le chemin exact du dossier répertoire. (ex : C:/Users/.../Downloads/Test)\n>>")

	path_directory[key] = path
	with open(PATH_DICT, 'w') as fw:
		json.dump(path_directory, fw, indent=4, sort_keys=True)
	print(f"{key}: {path} à été ajouté avec succès")


while True:
	path_directory = fill_path_directory()

	menu = input("Que désirez vous faire : "
				 "\n	1 : Renommez des fichiers "
				 "\n	2 : Ajouter des répertoires "
				 "\n	3 : Voir les répertoires accessibles "
				 "\n	4 : Supprimer un répertoire "
				 "\n	5 : Modifier les extensions "
				 "\n	6 : Quitter \n>>")
	try:
		if menu == '1':
			menu_rename() # Ouvre le sous menu permettant de choisi la façon de rename
		elif menu == '2':
			add_path_to_directory() # Ajoute un chemin au dictionnaire directory
		elif menu == '3':
			show_files() # Permet de voir le dictionnaire directory
		elif menu == '4':
			show_files()
			delete_folder_in_directory() # Supprime le répertoire ou le retire juste de la liste directory suivant l'option choisie
		elif menu == '5':
			print("Pas encore disponible ...")
			rename_extension() # Permet de renommer les extensions des fichiers sans toucher aux noms
		elif menu == '6' or menu == 'Q' or menu == 'q':
			break
	except FileExistsError:
		print("/!\ Un fichier existe déjà avec ce nom, cette opération n'est donc pas possible. /!\\")
	except KeyError:
		print("/!\ Cette clé ne correspond à aucun répertoire, cette opération n'est donc pas possible. /!\\")
