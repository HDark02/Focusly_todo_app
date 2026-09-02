from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
# from datetime import datetime
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import OneLineListItem, ThreeLineIconListItem
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.animation import Animation
# from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
# from kivy.uix.screenmanager import FadeTransition
import json
# from kivymd.uix.card import MDCard
import datetime 
import time
import threading
import os
import pygame
from pathlib import Path
pygame.mixer.init()

# from plyer import notification
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
# Window.size = (550, 840)
# Window._set_top(10)
# Window._set_left(450)
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
        screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.date_actuelle.text = f"Aperçu de l'activité du {datetime.datetime.now().strftime('%d/%m/%Y')}"
        screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.date_actuelle.text = f"Jusqu'au {datetime.datetime.now().strftime('%d/%m/%Y')}"
                   
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
                        date_time_full=time_time.split("  ")
                        self.start_alarm(date_time_full[1], date_time_full[0])
                        screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list.add_widget(new_task)

#########################################################################################
# screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id
  
    def ad_todo(self, task_input, date_date, time_time, task_note):
        if task_input.strip():  # Vérifie si la tâche n'est pas vide

            self.start_alarm(date_date, time_time)
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
        self.stop_alarm()
        for tache in todo_list.children:
            if tache.task_name == index_name:
                time_up_note= "Terminé à " +str(datetime.datetime.now().strftime("%H:%M:%S %p"))
                time_up = str(datetime.datetime.now().strftime("%H:%M:%S %p"))
                task_note = tache.note
                screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id.todo_list.size_hint_y -= 0.17
                screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.add_widget(Line_gestion(date= str(time_up),
                                                                                                                                                descrip= task_note,
                                                                                                                                                tache= tache.task_name,
                                                                                                                                                heure= time_up_note))
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
                    date_end_do=task["date_end_do"]
                    if task_input.strip():  # Vérifie si la tâche n'est pas vide
                        # date = str(datetime.datetime.now().strftime("%d/%m/%Y"))
                        screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.add_widget(Line_gestion(date=date_end_do,
                                                                                                                                            descrip= task_note,
                                                                                                                                            tache= task_input,
                                                                                                                                            heure= str(time_time)) )    
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
            # Rechercher le widget à sauvegarder

        try:
            if len(todo_list.children)==0:
                chemin_fichier="tasks_not_do.json"
                fichier = Path(chemin_fichier)
                try:
                    if fichier.is_file():
                        fichier.unlink()
                        print(f"✅ Fichier supprimé : {chemin_fichier}")
                    else:
                        print(f"⚠️ Le fichier '{chemin_fichier}' n'existe pas.")
                except PermissionError:
                    print(f"❌ Permission refusée pour supprimer : {chemin_fichier}")
                except OSError as e:
                    print(f"❌ Erreur lors de la suppression : {e}")
                todo_list.clear_widgets()
            for tache in todo_list.children:

                task_not_do={"task_not_do_title": tache.task_name,
                    "note_not_do": tache.note,
                    "time_not_do": tache.date_time
                    }

                tasks_not_do["all_data"].append(task_not_do)

                with open("tasks_not_do.json", "w") as file:
                    json.dump(tasks_not_do, file, indent= 4)
        except:
            pass

    def save_end_stop_task(self):
        tasks_end_do={
            "all_data_end": []
                }

        screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.remove_widget(screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.header)
        todo_list_end = screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end
            # Rechercher le widget à supprimer
        for tache in todo_list_end.children:
            try:
                task_not_do={"task_end_do_title": tache.tache,
                    "time_end_do": tache.heure,
                    "note_end_do": tache.descrip,
                    "date_end_do": tache.date
                    }

                tasks_end_do["all_data_end"].append(task_not_do)

                with open("tasks_end_not_do.json", "w") as file:
                    json.dump(tasks_end_do, file, indent= 4)
            except Exception as e:
                print(f"Error saving end task: {e}")
    def clean_end(self):
        tasks_end_do={
            "all_data_end": []
                }
        try:
            screen_manager.get_screen("gestion_des_vente_home").navig.termine_id.tache_termine_id.liste_of_task_end.clear_widgets()
            with open("tasks_end_not_do.json", "w") as file:
                json.dump(tasks_end_do, file, indent= 4)
        except Exception as e:
            print(f"Error saving end task: {e}")
    #########################################""
    def build(self):
        self.alarm_datetime = None
        self.sound_file = None
        self.alarm_thread = None
        self.stop_alarm_flag = False

        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("todo_main.kv"))
             
        return screen_manager
    def start_alarm(self, date_str, time_str):
        """Démarre le thread de l'alarme avec date complète."""
        try:
            date_init=date_str.split("/")
            time_init=time_str.split(":")
            day = int(date_init[0])
            month = int(date_init[1])
            year = int(date_init[2])
            hour = int(time_init[0])
            minute = int(time_init[1])

            self.alarm_datetime = datetime.datetime(year, month, day, hour, minute)

            if self.alarm_datetime <= datetime.datetime.now():
                screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.info_error.text = "⛔ La date/heure doit être dans le futur."
                screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.info_error.opacity = 1
                return
            screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.info_error.opacity = 0
            self.stop_alarm_flag = False
            self.alarm_thread = threading.Thread(target=self.run_alarm, daemon=True)
            self.alarm_thread.start()

        except ValueError:
            screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.info_error.text = "⛔ Entrée invalide. Vérifiez la date et l'heure."
            screen_manager.get_screen("gestion_des_vente_home").navig.ajout_id.ajouter_taches_screen_id.info_error.opacity = 1
    def run_alarm(self):
        """Boucle qui attend la date et l'heure de l'alarme."""
        while not self.stop_alarm_flag:
            now = datetime.datetime.now()
            if now >= self.alarm_datetime:
                # self.status_label.text = "⏰ ALARME !"
                self.play_alarm_sound()
                break
            time.sleep(1)

    def play_alarm_sound(self):
        """Joue le son de l'alarme en boucle jusqu'à arrêt."""
        try:
            pygame.mixer.music.load("alarm_song.mp3")
            pygame.mixer.music.play(-1)  # -1 = boucle infinie
        except:
            print("\a")  # Bip console

    def stop_alarm(self):
        """Arrête l'alarme immédiatement."""
        self.stop_alarm_flag = True
        pygame.mixer.music.stop()
        # self.status_label.text = "✅ Alarme arrêtée"


# #############################"""
if __name__=="__main__":
    Todo().run()
