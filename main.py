from kivymd.app import MDApp
from kivy.lang import Builder
from datetime import datetime
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import OneLineListItem, ThreeLineIconListItem
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivymd.uix.floatlayout import MDFloatLayout
import json
import os
class Line_gestion(OneLineListItem):
    date= StringProperty()
    descrip= StringProperty()
    tache= StringProperty()
    heure= StringProperty()
class Task_bord_card(MDFloatLayout):
    task_name= StringProperty()
    note= StringProperty()
    date_time=  StringProperty()
    image_name_out=  "check_icon.png"
class TodoendCard(ThreeLineIconListItem):
    text= StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()
    secondary_text_color = StringProperty("blue")
    font_size = StringProperty()
    # font_style = StringProperty()
    image_source = StringProperty()
class Todo(MDApp):
    def on_start(self):
        screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.date_actuelle.text = f"Aperçu de l'activité du {datetime.now().strftime('%d/%m/%Y')}"
        screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.date_actuelle.text = f"Jusqu'au {datetime.now().strftime('%d/%m/%Y')}"
                   
        self.load_data()
        self.load_end_task_data()
    #     screen_manager.current = "gestion_des_vente_home"
##########################################################################""
    def load_data(self):
        if os.path.exists("tasks_not_do.json"):
            with open("tasks_not_do.json", "r") as file:
                tasks = json.load(file)
                for task in tasks["all_data"]:
                    task_input=task["task_not_do_title"]
                    time_time=task["time_not_do"]
                    task_note=task["note_not_do"]
                    if task_input.strip():  # Vérifie si la tâche n'est pas vide
                        screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list.size_hint_y += 0.17
                        new_task=Task_bord_card(task_name=task_input,
                                                    date_time=str(time_time) ,
                                                    note = task_note)
                        screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list.add_widget(new_task)

#########################################################################################
# screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id
  
    def ad_todo(self, task_input, date_date, time_time, task_note):
        if task_input.strip():  # Vérifie si la tâche n'est pas vide
            new_task=Task_bord_card(task_name=task_input,
                                     date_time=str(time_time +"  "+ str(date_date)) ,
                                     note = task_note)
            screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list.size_hint_y += 0.17
            screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list.add_widget(new_task)
            screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.task_input.text = ""
            screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.date_date.text = ""
            screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.time_time.text = ""
            screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.note_task.text = ""
                        
            # Applique une animation pour faire apparaître la tâche
            animation = Animation(opacity=1, d=0.5)  # Animation d'apparition
            new_task.opacity = 0  # Commence avec une opacité de 0
            animation.start(new_task)
            self.save_tasks(task_name=task_input, date_time=str(time_time +"  "+ str(date_date)) ,note = task_note)

    def valide_task(self, index_name):
        todo_list = screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list
        # Rechercher le widget à supprimer
        for tache in todo_list.children:
            if tache.task_name == index_name:
                time_up = "Terminé à " +str(datetime.now().strftime("%H:%M:%S %p"))
                task_note = tache.note
                date = str(datetime.now().strftime("%d/%m/%Y"))
                screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list.size_hint_y -= 0.17
                screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.add_widget(Line_gestion(date= date,
                                                                                                                                                            descrip= task_note,
                                                                                                                                                            tache= tache.task_name,
                                                                                                                                                            heure= time_up))
                todo_list.remove_widget(tache)
    def save_end_tasks(self, task_name, date_time ,note):
            tasks_end_do={"all_data_end": [] }
            if os.path.exists("tasks_end.json"):
                with open("tasks_end.json", "r") as file:
                    tasks_end_do=json.load(file)
    
            task_end_do={"task_end_do_title": task_name,
            "note_end_do": note,
            "time_end_do": date_time
            }
    
            tasks_end_do["all_data_end"].append(task_end_do)
    
            with open("tasks_end.json", "w") as file:
                json.dump(tasks_end_do, file, indent= 4)
    def load_end_task_data(self):
        
        if os.path.exists("tasks_end_not_do.json"):
            
            with open("tasks_end_not_do.json", "r") as file:
                
                tasks_end_do=json.load(file)
                
                for task in tasks_end_do["all_data_end"]:
                
                    task_input=task["task_end_do_title"]
                    time_time=task["time_end_do"]
                    task_note=task["note_end_do"]
                    
                    if task_input.strip():  # Vérifie si la tâche n'est pas vide
                    
                        screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.add_widget(Line_gestion(date= str(date),
                                                                                                                                                                descrip= task_note,
                                                                                                                                                                tache= task_input,
                                                                                                                                                                heure= str(time_time)))      
    def save_tasks(self, task_name, date_time ,note):
        if os.path.exists("tasks_not_do.json"):
            with open("tasks_not_do.json", "r") as file:
                tasks_not_do=json.load(file)

                task_not_do={"task_not_do_title": task_name,
                "note_not_do": note,
                "time_not_do": date_time
                }
        else:
            tasks_not_do={
                "all_data": []
                    }
            task_not_do={"task_not_do_title": task_name,
                "note_not_do": note,
                "time_not_do": date_time
                }

        tasks_not_do["all_data"].append(task_not_do)

        with open("tasks_not_do.json", "w") as file:
            json.dump(tasks_not_do, file, indent= 4)

    def on_stop(self):
        self.save_stop_task()
        self.save_end_stop_task()
    def save_stop_task(self):
        tasks_not_do={
            "all_data": []
                }
                            
        todo_list = screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list
            # Rechercher le widget à supprimer
        for tache in todo_list.children:

            task_not_do={"task_not_do_title": tache.task_name,
                "note_not_do": tache.note,
                "time_not_do": tache.date_time
                }

            tasks_not_do["all_data"].append(task_not_do)

            with open("tasks_not_do.json", "w") as file:
                json.dump(tasks_not_do, file, indent= 4)

    def save_end_stop_task(self):
        tasks_end_do={
            "all_data_end": []
                }

        screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.remove_widget(screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.header)
        todo_list_end = screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end
            # Rechercher le widget à supprimer
        for tache in todo_list_end.children:
            try:
                task_not_do={"task_end_do_title": tache.heure,
                    "note_end_do": tache.descrip,
                    "time_end_do": tache.date
                    }

                tasks_end_do["all_data_end"].append(task_not_do)

                with open("tasks_end_not_do.json", "w") as file:
                    json.dump(tasks_end_do, file, indent= 4)
            except Exception as e:
                print(f"Error saving end task: {e}")
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("todo_main.kv"))
             
        return screen_manager

    #add date to the new task
    def on_save(self, instance, value, date_range):
        screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.date_date.text = str(value).replace("-", "/")

    def on_cancel(self, instance, value):
       pass
    #pick the date
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    #############################
    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save_time, on_cancel=self.on_cancel)
        time_dialog.open()
    def on_save_time(self, instance, time):
        screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.time_time.text = str(time)

if __name__=="__main__":
    Todo().run()
