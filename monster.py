import random
from datetime import datetime, timedelta

class Monster:
    def __init__(self, name, description, behavior, difficulty):
        self.name = name
        self.description = description
        self.behavior = behavior
        self.base_difficulty = difficulty
        self.current_difficulty = difficulty
        self.aggression = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.study_progress = 0
        self.revealed_info = {
            "name": True,
            "description": True,
            "behavior": False,
            "difficulty": False,
            "aggression": False,
            "intelligence": False
        }
        self.daily_interactions = 3

    def act(self):
        return random.choice(self.behavior)

    def interact(self, action):
        if self.daily_interactions <= 0:
            return "Non puoi interagire ulteriormente con questo mostro oggi."

        self.daily_interactions -= 1
        risk = self.current_difficulty * 0.1 + self.aggression * 0.05
        success = random.random() > risk

        if action == "observe":
            if success:
                self.study_progress += 1
                self.reveal_info()
                return f"Hai osservato con successo {self.name}. Progresso studio: {self.study_progress}/10"
            else:
                return f"{self.name} ha notato la tua presenza e {self.act()}"

        elif action == "communicate":
            if success:
                self.study_progress += 2
                self.reveal_info()
                return f"Sei riuscito a comunicare con {self.name}. Progresso studio: {self.study_progress}/10"
            else:
                return f"{self.name} ha reagito negativamente al tuo tentativo di comunicazione e {self.act()}"

        elif action == "test":
            if success:
                self.study_progress += 3
                self.reveal_info()
                return f"Il test su {self.name} ha avuto successo. Progresso studio: {self.study_progress}/10"
            else:
                return f"Il test su {self.name} è fallito. Il mostro {self.act()}"

        elif action == "sedate":
            if success:
                self.current_difficulty = max(1, self.current_difficulty - 1)
                return f"Sei riuscito a sedare {self.name} temporaneamente. La sua difficoltà è diminuita."
            else:
                self.current_difficulty = min(10, self.current_difficulty + 1)
                return f"Il tentativo di sedare {self.name} è fallito. Il mostro è diventato più agitato e difficile da gestire."

    def reveal_info(self):
        if self.study_progress >= 3 and not self.revealed_info["behavior"]:
            self.revealed_info["behavior"] = True
        if self.study_progress >= 5 and not self.revealed_info["difficulty"]:
            self.revealed_info["difficulty"] = True
        if self.study_progress >= 7 and not self.revealed_info["aggression"]:
            self.revealed_info["aggression"] = True
        if self.study_progress >= 9 and not self.revealed_info["intelligence"]:
            self.revealed_info["intelligence"] = True

    def reset_daily_interactions(self):
        self.daily_interactions = 3

monsters = [
    Monster("Shadowlurker", "Una creatura fatta di ombre che si muove silenziosamente", 
            ["si fonde con l'oscurità", "emette un sibilo basso", "tenta di avvolgere le vittime"], 3),
    Monster("Glitchbeast", "Un essere che sembra glitchare in e out dell'esistenza", 
            ["scompare e riappare", "emette suoni statici", "distorce la realtà circostante"], 5),
    Monster("Memoryphage", "Un'entità che si nutre dei ricordi delle sue vittime", 
            ["sussurra ricordi dimenticati", "cerca di toccare la testa delle vittime", "emette una luce ipnotica"], 4),
    Monster("Echomime", "Una creatura che imita perfettamente i suoni che sente", 
            ["ripete le ultime parole dette", "crea confusione con falsi rumori", "attira le vittime con suoni familiari"], 2),
    Monster("Cryptcrawler", "Un essere simile a un insetto gigante che si nasconde nei muri", 
            ["si muove attraverso le pareti", "tesse ragnatele invisibili", "emette un clicchettio inquietante"], 3),
    Monster("Neurovore", "Un parassita che si nutre dell'attività cerebrale", 
            ["fluttua nell'aria", "emette un ronzio ipnotico", "cerca di attaccarsi alla testa delle vittime"], 6),
    Monster("Chronophage", "Un mostro che sembra alterare il flusso del tempo intorno a sé", 
            ["invecchia rapidamente gli oggetti vicini", "crea loop temporali locali", "si muove a velocità imprevedibili"], 7),
    Monster("Plasmamorph", "Un essere fatto di plasma che può assumere varie forme", 
            ["cambia forma continuamente", "emette una luce pulsante", "cerca di inglobare oggetti e creature"], 5),
    Monster("Voidwalker", "Una creatura che sembra provenire dal vuoto stesso", 
            ["crea zone di buio assoluto", "si teletrasporta", "sussurra segreti cosmici"], 8),
    Monster("Fractalbeast", "Un mostro la cui forma segue schemi frattali complessi", 
            ["si divide in copie più piccole", "crea illusioni geometriche", "si ricompone in forme sempre diverse"], 6),
    Monster("Echosiren", "Un'entità che attira le vittime con canti ipnotici", 
            ["emette melodie irresistibili", "crea illusioni sonore", "si nutre delle emozioni delle vittime"], 4),
    Monster("Quantumshifter", "Un essere che esiste in stati quantici sovrapposti", 
            ["appare in più luoghi contemporaneamente", "passa attraverso oggetti solidi", "altera la probabilità degli eventi"], 9),
    Monster("Mindweaver", "Una creatura che può manipolare i pensieri altrui", 
            ["proietta illusioni mentali", "legge i pensieri superficiali", "induce stati di confusione"], 7),
    Monster("Gravitytwister", "Un mostro che altera la gravità intorno a sé", 
            ["fa levitare oggetti e creature", "crea zone di gravità invertita", "schiaccia le vittime con campi gravitazionali"], 6),
    Monster("Entropywraith", "Un'entità che accelera il decadimento di tutto ciò che tocca", 
            ["fa arrugginire i metalli istantaneamente", "decompone la materia organica", "invecchia rapidamente le sue vittime"], 8),
    Monster("Dreamleech", "Una creatura che si nutre dei sogni e degli incubi", 
            ["induce il sonno nelle vittime", "crea allucinazioni vivide", "ruba frammenti di memoria"], 5),
    Monster("Paradoxspider", "Un aracnide multidimensionale che tesse ragnatele di realtà", 
            ["crea paradossi spazio-temporali", "intrappola le vittime in loop logici", "si muove tra dimensioni parallele"], 9),
    Monster("Whisperwind", "Un essere etereo che trasporta voci e segreti", 
            ["sussurra informazioni criptiche", "crea correnti d'aria innaturali", "ruba le voci delle vittime"], 3),
    Monster("Chaoshydra", "Un mostro con multiple teste che incarnano diversi aspetti del caos", 
            ["genera eventi casuali", "si rigenera quando viene ferito", "emette raggi di energia caotica"], 8),
    Monster("Mirrorwalker", "Una creatura che vive all'interno degli specchi", 
            ["emerge dagli specchi", "intrappola le vittime nei riflessi", "distorce le immagini riflesse"], 5),
    Monster("Nebulaghoul", "Un essere composto da gas e polvere cosmica", 
            ["si dissolve in una nube tossica", "crea mini supernove", "assorbe la luce circostante"], 7),
    Monster("Chronospecter", "Un fantasma che esiste fuori dal tempo lineare", 
            ["mostra visioni del passato e del futuro", "invecchia o ringiovanisce le vittime", "crea anomalie temporali"], 8),
    Monster("Biomechmorph", "Un ibrido di carne e macchina in continua evoluzione", 
            ["si adatta rapidamente all'ambiente", "assimila tecnologia", "infetta altri esseri con naniti"], 6),
    Monster("Psychevampire", "Un'entità che si nutre dell'energia psichica", 
            ["drena la forza vitale", "induce stati di depressione", "si nutre di emozioni intense"], 5),
    Monster("Realityglitch", "Una creatura che causa malfunzionamenti nella realtà", 
            ["crea zone di realtà distorta", "causa errori nella fisica", "genera effetti visivi glitch"], 7),
    Monster("Voidmaw", "Un essere con una bocca che conduce a un vuoto infinito", 
            ["risucchia oggetti e creature", "emette un vuoto assoluto", "digerisce la realtà stessa"], 9),
    Monster("Echolocator", "Un predatore che usa l'ecolocalizzazione per cacciare", 
            ["emette onde sonore disorientanti", "vede attraverso i muri", "crea illusioni acustiche"], 4),
    Monster("Quantumentangler", "Una creatura che manipola l'entanglement quantistico", 
            ["collega oggetti distanti", "teletrasporta parti di sé", "crea copie quantistiche di se stesso"], 8),
    Monster("Memorymosaic", "Un essere composto dai ricordi perduti nelle Backrooms", 
            ["proietta frammenti di memorie aliene", "assorbe i ricordi delle vittime", "crea labirinti di ricordi"], 6),
    Monster("Nullshadow", "Un'ombra vivente che cancella ciò che tocca", 
            ["cancella temporaneamente oggetti e creature", "crea zone di non-esistenza", "si nutre dell'essenza vitale"], 7),
    Monster("Fractalphage", "Un parassita che infetta la realtà con schemi frattali", 
            ["trasforma l'ambiente in strutture frattali", "si replica all'infinito", "distorce la percezione spaziale"], 6),
    Monster("Enigmasphinx", "Una creatura che pone enigmi mortali", 
            ["pone indovinelli cosmici", "intrappola le vittime in puzzle viventi", "si nutre della frustrazione mentale"], 5),
    Monster("Quantumschrodinger", "Un felino multidimensionale in perpetuo stato di sovrapposizione", 
            ["esiste e non esiste simultaneamente", "crea paradossi di osservazione", "altera la realtà quando osservato"], 8),
    Monster("Memeticdoppelganger", "Un'entità che copia e sostituisce altre creature", 
            ["assume l'aspetto delle vittime", "diffonde false informazioni", "crea confusione identitaria"], 6),
    Monster("Looptrapper", "Un predatore che intrappola le vittime in loop temporali", 
            ["crea mini time loop", "si nutre dell'energia temporale", "invecchia fuori dai loop"], 7),
    Monster("Datasphere", "Una sfera vivente di pura informazione", 
            ["assorbe e proietta dati", "hackera la realtà circostante", "sovrascrive i ricordi delle vittime"], 6),
    Monster("Voidweaver", "Un artigiano che tesse la stoffa della realtà", 
            ["ripara o danneggia il tessuto dello spazio-tempo", "crea portali dimensionali", "altera le leggi fisiche locali"], 9),
    Monster("Echochamber", "Una creatura che amplifica e distorce i suoni", 
            ["crea caos acustico", "si nutre delle vibrazioni sonore", "comunica attraverso echi complessi"], 4),
    Monster("Probabilityshifter", "Un essere che manipola le probabilità", 
            ["causa eventi altamente improbabili", "altera il destino", "crea zone di fortuna o sfortuna estrema"], 8),
    Monster("Cognitohazard", "Un'entità la cui mera percezione è pericolosa", 
            ["causa danni mentali a chi lo osserva", "si diffonde attraverso il pensiero", "corrompe le menti con la sua presenza"], 10)
]

def add_daily_monster():
    today = datetime.now().date()
    seed = int(today.strftime("%Y%m%d"))
    random.seed(seed)
    
    adjectives = ["Spaventoso", "Misterioso", "Terrificante", "Enigmatico", "Letale", "Bizzarro", "Inquietante"]
    nouns = ["Predatore", "Spettro", "Abominio", "Entità", "Creatura", "Aberrazione", "Mostro"]
    
    name = f"{random.choice(adjectives)} {random.choice(nouns)} {seed % 1000}"
    description = f"Una creatura misteriosa scoperta il {today}"
    behaviors = [
        "si muove in modo imprevedibile",
        "emette suoni inquietanti",
        "altera l'ambiente circostante",
        "cerca di comunicare in modi strani",
        "mostra abilità mai viste prima"
    ]
    difficulty = random.randint(1, 10)
    
    new_monster = Monster(name, description, behaviors, difficulty)
    monsters.append(new_monster)
    return new_monster

def get_current_monsters():
    today = datetime.now().date()
    start_date = datetime(2023, 1, 1).date()  # Data di inizio arbitraria
    days_passed = (today - start_date).days
    
    current_monsters = monsters[:] # Copia la lista originale
    
    # Aggiungi un nuovo mostro per ogni giorno passato
    for _ in range(days_passed):
        add_daily_monster()
    
    # Resetta le interazioni giornaliere per tutti i mostri
    for monster in current_monsters:
        monster.reset_daily_interactions()
    
    return current_monsters
