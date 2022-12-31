import math
import random


# divisione per 0, devo rivedere la fitness ed eval come vengono prese... per il resto funziona
print("------------------ Programma per minimizzare una funzione f(x) a 4 variabili ------------------")
print("f(x) = x0a + x1b + x2c + x3d = y")
x0 = int(input("Inserire x0: "))
x1 = int(input("Inserire x1: "))
x2 = int(input("Inserire x2: "))
x3 = int(input("Inserire x3: "))
y = int(input("Inserire y: "))

print("\nL'equazione risulta: f(x) = " + str(x0) + "a + " + str(x1) + "b + " + str(x2) + "c + " + str(x3) + "d = " + str(y) + "\n")


# i valori da trovare per a, b, c e d devono essere compresi tra 0 e y
N_CROMOSOMI = 6 # numero "casuale"
LUNGHEZZA_CROMOSOMA = 4

def accoppiamento(genitore1, genitore2):
    crossover = random.randint(1, LUNGHEZZA_CROMOSOMA - 1)
    # scambiamo i geni tra i genitori
    figlio = []
    for i in range(crossover):
        figlio.append(genitore1[i])
    for i in range(crossover, LUNGHEZZA_CROMOSOMA):
        figlio.append(genitore2)

    return figlio


def evaluation(cromosoma):
    result = abs(((x0*cromosoma[0]) + (x1*cromosoma[1]) + (x2*cromosoma[2]) + (x3*cromosoma[3])) - y)
    return result


def fitness(valutazione):
    return 1/valutazione



cromosomi = []
best = []
best_eval = 999999

while best_eval > 0:
    for i in range (N_CROMOSOMI):
        temp = []
        for j in range (LUNGHEZZA_CROMOSOMA):
            temp.append(random.randint(0, y))
        cromosomi.append(temp)
        print("cromosomi[" + str(i) + "]: " + str(cromosomi[i]))


    print("\nValutazione:")
    valutati = []
    for element in cromosomi:
        valutati.append(evaluation(element))
        print("valutazione di " + str(element) + ": " + str(evaluation(element)))
        if best == [] or best_eval > evaluation(element):
            best_eval = evaluation(element)
            best = element

    # print(str(c))

    crossover_rate = 0.25

    randomici = []
    genitori = []
    for i in range(N_CROMOSOMI):
        n = 0
        while (n == 0 or n == 1):
            n = random.random()
        randomici.append(n)
        if (randomici[i] < crossover_rate):
            genitori.append(cromosomi[i])
        #  print(randomici[i])

    # se il numero randomico associato al cromosoma i è < crossover_rate, il cromosoma i diviene un genitore

    cromosomi = []

    for genitore1 in cromosomi:
        for genitore2 in cromosomi:
            if genitore1 != genitore2:
                cromosomi.append(accoppiamento(genitore1, genitore2))

    

    # MUTAZIONE
    geni_totali = N_CROMOSOMI * LUNGHEZZA_CROMOSOMA
    numero_mutazioni = math.floor(geni_totali * 0.1)

    print("\n")


print("\n\n\n\nMiglior individuo:\n")
print(str(best), " eval: ", best_eval)