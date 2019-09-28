from tkinter import *
import os


	
#Основная функция создания заметок
def create_notes():

	#Если нужно просто записать текст не кодируя его
	def get_text():
		inputLabel = write_label.get()
		inputText = write_text.get("1.0","end-1c")
		note=open('NC__'+inputLabel+'.txt','w')
		note.write(inputText)
		note.close()
	
	#Если кодируешь текст
	#Открытвает окно и предлагает ввести код (0-52) Шифр Цезаря	
	def create_pass():
		
		#Сам процесс кодировки
		def coding_text():
			inputPass = crypto_pass.get()
			crypto_pass_window.destroy()
			inputLabel = write_label.get()
			inputText = write_text.get("1.0","end-1c")
			
			arr1 = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч',
			'Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с',
			'т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ','.','?','!','1','2','3','4','5','6','7','8','9',
			'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
			'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ',',';',':']

			arr2 = []
			for i in range(len(arr1)):
				arr2.append(arr1[i])

			def arr2_change():
				for i in range(int(inputPass)):
					arr2.append(arr2[0])
					arr2.remove(arr2[0])

			arr2_change()	

			msgc = ''
			for i in inputText:
				for j in range(len(arr1)):
					if i == arr1[j]:
						msgc+=arr2[j]
			note=open('C__'+inputLabel+'.txt','w')
			note.write(msgc)
			note.close()


		crypto_pass_window = Toplevel(window)
		crypto_pass_window.title("Create password")
		say_create_pass = Label(crypto_pass_window, text="Придумайте пароль(Только цифры, до 6 знаков)", font=("Ubuntu", 25))
		say_create_pass.pack()
		crypto_pass = Entry(crypto_pass_window)
		crypto_pass.pack()
		create_pass_button = Button(crypto_pass_window, text="Create", command=coding_text)
		create_pass_button.pack()

	window = Toplevel(root)
	window.title('Create Note')
	title_name = Label(window, text="↓Название ↓↓Текст", font=("Ubuntu", 14))
	title_name.pack()
	write_label = Entry(window, text="Название", font=("Ubuntu", 14))
	write_label.pack()
	write_text = Text(window, width=50, height=20, font=("Ubuntu", 14))
	write_text.pack()
	button_free_create = Button(window, text="Создать", command=get_text)
	button_coding_create = Button(window, text="Закодировать", command=create_pass)
	button_free_create.pack()
	button_coding_create.pack()

#Чтение заметок
def all_notes_list():
	
	def edit_note():
		
		def save_edit():
			text = edit_text.get("1.0","end-1c")
			note=open(get_listbox_name,'w')
			note.write(text)
			note.close()
			edit_window.destroy()

		edit_window = Toplevel(window)
		edit_window.title("Edit note")
		select_note = list_notes.curselection()
		get_listbox_name = list_notes.get(select_note)
		text_note_after = open(get_listbox_name)
		text_note = text_note_after.read()
		
		def first2(s):
			return s[:2]

		if first2(get_listbox_name) == "C_":
			#Просит ввести код для дешифровки
			def confirm_pass():
				#Дешифровка текста
				def decoding_text():
					
					def coding_text():
						
						text = edit_text.get("1.0","end-1c")

						arr1 = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч',
						'Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с',
						'т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ','.','?','!','1','2','3','4','5','6','7','8','9',
						'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
						'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ',',';',':']

						arr2 = []
						for i in range(len(arr1)):
							arr2.append(arr1[i])

						def arr2_change():
							for i in range(int(input_pass)):
								arr2.append(arr2[0])
								arr2.remove(arr2[0])

						arr2_change()
						msgd=""
				
						for i in text:
							for j in range(len(arr1)):
								if i==arr1[j]:
									msgd+=arr2[j]


						
						note=open(get_listbox_name,'w')
						note.write(msgd)
						note.close()
						edit_window.destroy()

					edit_decoding_text = Toplevel(edit_window)
					edit_decoding_text.title("Read Note")
					input_pass = confirm_pass.get()

					arr1 = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч',
					'Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с',
					'т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ','.','?','!','1','2','3','4','5','6','7','8','9',
					'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
					'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',',',';',':']

					arr2 = []
					for i in range(len(arr1)):
						arr2.append(arr1[i])

					def arr2_change():
						for i in range(int(input_pass)):
							arr2.append(arr2[0])
							arr2.remove(arr2[0])

					arr2_change()
					msgd=""
			
					for i in text_note:
						for j in range(len(arr1)):
							if i==arr2[j]:
								msgd+=arr1[j]

							
					title_note = Label(edit_decoding_text, text=get_listbox_name)
					title_note.pack()
					edit_text = Text(edit_decoding_text, font=("Ubuntu", 14))
					edit_text.insert(1.0, msgd)
					edit_text.pack()
					save_edit_button = Button(edit_decoding_text, text="Сохранить", font=("Ubuntu", 20), command=coding_text)
					save_edit_button.pack()	

				say_confirm_pass = Label(edit_window, text="Введите ваш пароль", font=("Ubuntu", 25))
				say_confirm_pass.pack()
				confirm_pass = Entry(edit_window)
				confirm_pass.pack()
				confirm_pass_button = Button(edit_window, text="Подтвердить", command=decoding_text)
				confirm_pass_button.pack()
			open_note = open(get_listbox_name)
			read_note = open_note.read()
			confirm_pass()
		
			
		if first2(get_listbox_name) == "NC":
			title_note = Label(edit_window, text=get_listbox_name)
			title_note.pack()
			edit_text = Text(edit_window, font=("Ubuntu", 14))
			edit_text.insert(1.0, text_note)
			edit_text.pack()
			save_edit_button = Button(edit_window, text="Сохранить", width=10,heigh=3,font=("Ubuntu", 20), command=save_edit)
			save_edit_button.pack()

	def delete_note():
		select_note = list_notes.curselection()
		get_listbox_name = list_notes.get(select_note)
		os.remove(get_listbox_name)

	#Функция чтения заметок и их декодирования
	def read_note():
		#Вызывает окно в которое либо записывает текст, либо просит ввести шифр
		read_window = Toplevel(window)
		read_window.title("Read Note")
		select_note = list_notes.curselection()
		get_listbox_name = list_notes.get(select_note)
	

		def first2(s):
			return s[:2]

		if first2(get_listbox_name) == "C_":
			#Просит ввести код для дешифровки
			def confirm_pass():
				#Дешифровка текста
				def decoding_text():
					read_decoding_text = Toplevel(read_window)
					read_decoding_text.title("Read Note")
					input_pass = confirm_pass.get()

					arr1 = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч',
					'Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с',
					'т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ','.','?','!','1','2','3','4','5','6','7','8','9',
					'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
					'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',',',';',':']

					arr2 = []
					for i in range(len(arr1)):
						arr2.append(arr1[i])

					def arr2_change():
						for i in range(int(input_pass)):
							arr2.append(arr2[0])
							arr2.remove(arr2[0])

					arr2_change()
					msgd=""
			
					for i in read_note:
						for j in range(len(arr1)):
							if i==arr2[j]:
								msgd+=arr1[j]
					
					read_label = Label(read_decoding_text,text=msgd,font=("Ubuntu", 14))
					read_label.pack()

				say_confirm_pass = Label(read_window, text="Введите ваш пароль", font=("Ubuntu", 25))
				say_confirm_pass.pack()
				confirm_pass = Entry(read_window)
				confirm_pass.pack()
				confirm_pass_button = Button(read_window, text="Create", command=decoding_text)
				confirm_pass_button.pack()
			open_note = open(get_listbox_name)
			read_note = open_note.read()
			confirm_pass()
		
			
		if first2(get_listbox_name) == "NC":
			open_note = open(get_listbox_name)
			read_note = open_note.read()
			read_label = Label(read_window, text=read_note, font=("Ubuntu", 14))
			read_label.pack()
	#Выводит окно со всеми заметками и кнопку для их прочтения и удаления
	window = Toplevel(root)
	window.title('Notes List')
	window.geometry("380x300")

	name_notes = []
	dir_notes = os.getcwd()
	for file in os.listdir(dir_notes):
		if file.endswith(".txt"):
			name_notes.append(file)

	read_button = Button(window, text="Читать", command=read_note)
	read_button.pack(side=TOP)	
	delete_button = Button(window, text="Удалить", command=delete_note)
	delete_button.pack(side=BOTTOM)
	edit_button = Button(window, text="Изменить", command=edit_note)
	edit_button.pack(side=BOTTOM)
	list_notes = Listbox(window,width=50,heigh=16, font=("Ubuntu", 14))
	list_notes.pack(side=BOTTOM)
	
	for key in name_notes:
		list_notes.insert(0, key)

root=Tk()
root.title('Notes')
root.geometry("280x260")
frame_bot = Frame(root)
frame_bot2 = Frame(root)
frame_bot3 = Frame(root)

button_all_notes = Button(frame_bot2, text='☰', bg='lightgreen', font=("Ubuntu", 25), heigh=2, width=5, command=all_notes_list)
button_create_note = Button(frame_bot3, text='Create', bg='lightblue', font=("Ubuntu", 25),heigh=2, width=9, command=create_notes)

frame_bot.pack()
frame_bot2.pack()
frame_bot3.pack()

button_all_notes.pack(side=TOP, pady=16)
button_create_note.pack()

root.mainloop()
