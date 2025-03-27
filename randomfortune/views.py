from django.shortcuts import render
import random

# Create your views here.

fortuneList = [
    "A tête bien faite, Rouge casquette",
    "Un moustachu, dans ton salon, s'étend de tout son long.",
    "Un grand péril sur le monde s'abat, Un héros surgit et en guerre s'en va.",
    "Le héros enquête de rares trésors, Préférera toujours la clé à l'or.",
    "Celle qui, le soleil cherche à éviter, Y parvient avec grande dignité.",
    "Paré de vert, le héros est un bleu, Il porte en lui le pouvoir des dieux.",
    "Quand le Mal, 1000 visages revêt, De masque, change sans arrêt !",
    "Le casque, les chutes amortit, Mais de toute élégance fait fi.",
    "Dans un autre château, tu dois aller, Ce ne sera sûrement pas le dernier.",
    "Qui avec le feu, joue, Ne se brûle pas à tous les coups."
]


def fortune(request):
    fortune = random.choice(fortuneList)
    context = {
        "fortune": fortune
    }
    return render(request, 'randomfortune/fortune.html', context) 