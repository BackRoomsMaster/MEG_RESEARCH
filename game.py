from monster import Monster, get_current_monsters, add_daily_monster
import random

class ContainmentUnit:
    def __init__(self, monster):
        self.monster = monster
        self.base_security_level = random.randint(1, 5)
        self.current_security_level = self.base_security_level

    def interact(self, action):
        escape_risk = (self.monster.current_difficulty * 0.1 + self.monster.aggression * 0.05) / self.current_security_level
        if random.random() < escape_risk:
            return f"ATTENZIONE: {self.monster.name} sta tentando di fuggire!"
        else:
            result = self.monster.interact(action)
            if "successo" in result:
                self.current_security_level = min(10, self.current_security_level + 0.5)
            elif "fallito" in result:
                self.current_security_level = max(1, self.current_security_level - 0.5)
            return result

class Game:
    def __init__(self):
        self.monsters = get_current_monsters()
        self.containment_units = [ContainmentUnit(monster) for monster in self.monsters]

    def play(self):
        print("Benvenuto alle Backrooms - Laboratorio di Contenimento M.E.G.")
        while True:
            print("\nAzioni disponibili:")
            print("1. Osserva le unità di contenimento")
            print("2. Interagisci con un'unità")
            print("3. Aggiorna (simula un nuovo giorno)")
            print("4. Esci")
            
            choice = input("Cosa vuoi fare? ")
            
            if choice == "1":
                self.observe_units()
            elif choice == "2":
                self.interact_with_unit()
            elif choice == "3":
                self.daily_update()
            elif choice == "4":
                print("Grazie per aver giocato. Arrivederci!")
                break
            else:
                print("Scelta non valida. Riprova.")

    def observe_units(self):
        for i, unit in enumerate(self.containment_units, 1):
            print(f"\nUnità {i}:")
            print(f"Mostro: {unit.monster.name}")
            if unit.monster.revealed_info["description"]:
                print(f"Descrizione: {unit.monster.description}")
            if unit.monster.revealed_info["behavior"]:
                print(f"Comportamenti osservati: {', '.join(unit.monster.behavior)}")
            if unit.monster.revealed_info["difficulty"]:
                print(f"Livello di difficoltà: {unit.monster.current_difficulty}")
            if unit.monster.revealed_info["aggression"]:
                print(f"Livello di aggressività: {unit.monster.aggression}")
            if unit.monster.revealed_info["intelligence"]:
                print(f"Livello di intelligenza: {unit.monster.intelligence}")
            print(f"Livello di sicurezza: {unit.current_security_level:.1f}")
            print(f"Progresso studio: {unit.monster.study_progress}/10")
            print(f"Interazioni rimanenti oggi: {unit.monster.daily_interactions}")

    def interact_with_unit(self):
        unit_num = int(input("Con quale unità vuoi interagire? (1-{}) ".format(len(self.containment_units)))) - 1
        if 0 <= unit_num < len(self.containment_units):
            unit = self.containment_units[unit_num]
            if unit.monster.daily_interactions > 0:
                print(f"\nInteragendo con {unit.monster.name}")
                print("Azioni disponibili:")
                print("1. Osserva")
                print("2. Comunica")
                print("3. Esegui test")
                print("4. Tenta di sedare")
                action_choice = input("Cosa vuoi fare? ")
                
                if action_choice == "1":
                    result = unit.interact("observe")
                elif action_choice == "2":
                    result = unit.interact("communicate")
                elif action_choice == "3":
                    result = unit.interact("test")
                elif action_choice == "4":
                    result = unit.interact("sedate")
                else:
                    result = "Azione non valida."
                
                print(result)
            else:
                print("Non puoi interagire ulteriormente con questo mostro oggi.")
        else:
            print("Numero di unità non valido.")

    def daily_update(self):
        new_monster = add_daily_monster()
        self.monsters.append(new_monster)
        self.containment_units.append(ContainmentUnit(new_monster))
        print(f"Nuovo mostro scoperto: {new_monster.name}")
        
        for monster in self.monsters:
            monster.reset_daily_interactions()
        
        print("Un nuovo giorno è iniziato. Le interazioni con i mostri sono state resettate.")

if __name__ == "__main__":
    game = Game()
    game.play()
