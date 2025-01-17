import time
from random import *

czas_decyzji = 30           #czas po kórym zakończenie jest dobierane automatycznie


print("Witaj w grze korpos!")           #wstęp pokazujący się po uruchomieniu gry
print("Masz 30 lat i znikome szanse na realizacje swoich marzeń.")
print("Pracujesz w korporacji, której nienawidzisz. Prawie cały swój czas poświecasz na pracę, równolegle zarabiając minimalną krajową.")
print("Ledwo wiążesz koniec z końcem. Jednak wciąż wieżysz, że los jeszcze się do ciebie uśmiechnie.")


def wybór_spieszysz():
    input("jeśli jesteś gotowy, wciśnij ENTER")
    start = int(time.time())                                                   #pomiar czasu w momencie potwierdzenia gotowosci gracza

    print("Budzisz się rano. Boli cię głowa. Jest poniedziałek. Patrzysz na zegarek,  który pokazuje godzinę 9:04.") 
    print("Pracę zaczynasz o 8:00, więc jesteś już spóźniony.") 
    print("Możesz wybiec z domu w pośpiechu się ubierając lub wstać  na spokojnie realizujac codzienną rutynę.")

    print("Czy się spieszysz? (wpisz TAK lub NIE)")
    zakończenie = 0
    spieszysz = input ("> ")


    end = int(time.time())                                                     #pomiar czasu w momencie podjęcia dezycji przez gracza

    if ((spieszysz == "TAK" or "NIE" ) and (end-start >= czas_decyzji)):
        print("zajęło to zbyt długo, los zdecydował za ciebie")
        for i in range(1):                                                      #procedura losowania zaakończenia
            zakończenie = randrange(1, 6)
    elif ((spieszysz == "TAK") and (end-start < czas_decyzji)):
        print("Jeszcze się dobrze nie obudziłeś, a już byłeś w połowie drogi do windy i wiązałeś krawat.")
        print("Przy windzie spotykasz sąsiadkę, Panią Wiesię, która wraca z zakupów. ")
        print("Kobieta prosi cię byś jej pomógł zanieść zakupy do domu.")
        print("Pomożesz sąsiadce? (wpisz TAK lub NIE)")
        zakończenie = wybór_pomozesz()
    elif ((spieszysz == "NIE") and (end-start < czas_decyzji)):
        print("Wstajesz, spokojnie odbywasz poranną toaletę, ubierasz się i wychodzisz.")
        print("Jesteś jednak głodny.")
        print("Idziesz coś zjeść? (wpisz TAK lub NIE)")
        zakończenie = wybór_zjesc()
    else:
        print ("należy wpisać TAK lub NIE")
        zakończenie = wybór_spieszysz()                    #funkcja wraca do początku w przypadku podania nieprzewidzianej odpowiedzi
    return zakończenie
         

def wybór_pomozesz():
    pomozesz = input(">")
    if (pomozesz == "TAK"):
        print("Pani Wiesia jest ci wdzięczna. Przy okazji rozmawiacie. Opowiadasz jej o swoich problemach w pracy.") 
        print("Jednak w końcu nadzchodzi czas, by kontynuować podróż do siedziby firmy.")
        print("Wychodzisz z bloku i biegniesz do pracy. ")
        print("Po wejściu do firmy z ulgą stwierdzasz brak obecności szefowej. Dziarskim krokiem wchodzisz do swojego pokoju, gdzie niespodziewanie czeka na ciebie szefowa.") 
        print("Oznajmia ci ona, że dostałeś awans.")
        print("Okazało się, że Pani Wiesia posiada koneksje w świecie biznesu. Zadbała ona o to by twoja kariera się rozwijała.")
        zakończenie = 1
    elif (pomozesz == "NIE"):
        print ("Nie masz czasu. Ignorujesz prośbę, wbiegasz do windy, przewracając przypadkiem  sąsiadkę i zjeżdżasz na parter.")
        print ("Pani Wiesia jest zbulwersowana twoim zachowaniem.")
        print ("Wychodzisz z bloku i biegniesz do pracy.") 
        print ("Po wejściu do firmy z ulgą stwierdzasz brak obecności szefowej. Dziarskim krokiem wchodzisz do swojego pokoju, gdzie niespodziewanie czeka na ciebie szefowa.")
        print ("Oznajmia ci ona, że już tu nie pracujesz.")
        print ("Okazało się, że Pani Wiesia posiada koneksje w świecie biznesu. Teraz już żadna licząca się na rynku firma cię nie zatrudni.")
        zakończenie = 2
    else:
         print ("należy wpisać TAK lub NIE")
         zakończenie = wybór_pomozesz()
    return zakończenie

def wybór_zjesc():
    jesc = input(">")
    if (jesc == "TAK"):
        print("Jesteś spóźniony, ale przecież ważniejsze jest jedzenie.") 
        print("Wchodzisz do osiedlowego sklepu i kupujesz coś na ząb. ")
        print("Spotykasz przy kasie atrakcyjną kobietę. Ucinacie sobie pogawendkę o jakosći sklepów w Polsce. W pewnym momencie mówi ci, że musi już iść.")
        print("Pytasz ją o numer? (wpisz TAK lub NIE)")
        zakończenie = wybór_numer()
    elif (jesc == "NIE"):
        print("Praca jest dla ciebie wszystkim. Bez niej przecież stracisz środki do życia.")
        print("Lecz w pewnym momencie pojawia ci się myśl w głowie, by coś zmienić.")
        print("Odważysz się? (wpisz TAK lub NIE)")
        zakończenie = wybór_odwazysz()
    else:
        print ("należy wpisać TAK lub NIE")
        zakończenie = wybór_zjesc()
    return zakończenie

def wybór_numer():
    numer = input(">")
    if (numer == "TAK"):
        print("Udało się. W kolejnym etapie zakładacie dużą, szczęśliwą rodzinę, a ty niesiony na fali sukcesu znajdujesz lepszą pracę.")
        zakończenie = 4
    elif (numer == "NIE"):
        print("Rozmowa zainspirowała cię do otworzenia sklepu osiedlowego, który z czasem rozrósł się do ogólnopolskiej sieci sklepów.")
        zakończenie = 5
    else:
        print ("należy wpisać TAK lub NIE")
        zakończenie = wybór_numer()
    return zakończenie

def wybór_odwazysz():
    odwazysz = input(">")
    if (odwazysz == "TAK"):
        print("Wychodzisz ze swojej strefy komfortu. Postanawiasz sprzedać wszystko co posiadasz.") 
        print("Za te pieniądze kupujesz bilet w jedną stronę do upragnionego raju.")
        zakończenie = 3
    elif (odwazysz == "NIE"):
        print("Postanowiłeś pozostać przy tym co znane. W wyniku spóźnienia obcięli ci premię. By nadrobić stratę zacząłeś brać coraz więcej nadgodzin.") 
        print("Twoje życie praktycznie przreniosło się do biura. Twój organizm nie wytrzymuje takiego obciążenia.")
        zakończenie = 6
    else:
        print ("należy wpisać TAK lub NIE")
        zakończenie = wybór_odwazysz()
    return zakończenie

zakończenie = wybór_spieszysz()


if (zakończenie == 1):
    print("FINANSOWO JESTEŚ USTAWIONY DO KOŃCA ŻYCIA, LECZ DALEJ NIE ZREALIZOWAŁEŚ MARZEŃ I JESTEŚ NIESZCZĘŚLIWY")
    print("koniec gry")
elif (zakończenie == 2):
    print("KOŃCZYSZ NA ULICY JAKO ŻEBRAK")
    print("koniec gry")
elif (zakończenie == 3): 
    print("LECISZ NA HAWAJE I ŻYJESZ JAKBY NIE MIAŁO BYĆ JUTRA")
    print("koniec gry")
elif (zakończenie == 4): 
    print("MASZ RODZINĘ I DOBRĄ PRACĘ")
    print("koniec gry")
elif (zakończenie == 5): 
    print("ZAKŁADASZ SIEĆ SKLEPÓW 'ROPUCHA' I WRESZCIE MOŻESZ SPEŁNIAĆ MARZENIA")
    print("koniec gry")
elif (zakończenie == 6): 
    print("ZAPRACOWUJESZ SIĘ NA ŚMIERĆ")
    print("koniec gry")
else:
    print("spróbuj jeszcze raz")