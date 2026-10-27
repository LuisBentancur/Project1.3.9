from __future__ import print_function

"""
Pude ver que el codigo estaba mal asi que lo arregle 
Perdon por modificarlo el responsable fue Luis Bentancur 

Torneo del dilema del prisionero iterado.
Cada jugador utiliza una estrategia para decidir si coopera o traiciona.
El torneo enfrenta a cada jugador con los anteriores durante una cantidad
aleatoria de rondas (entre 100 y 200). Se registran las jugadas, los puntos
y una tabla comparativa en el archivo tournament.txt.
Las estrategias de los 20 jugadores están definidas en obtener_accion()
(en el código original se conserva el nombre get_action por compatibilidad).
"""

import random


def play_round(player1, player2, history1, history2, score1, score2):
    """Juega una ronda entre dos jugadores.

    Consulta la estrategia de cada jugador, guarda sus acciones en el historial
    y actualiza los puntajes según la combinación de cooperación y traición.
    Devuelve los historiales y los puntajes actualizados de ambos jugadores."""
    
    RELEASE = 0 # (R): recompensa cuando ambos jugadores cooperan
    TREAT = 100 # (T): beneficio por traicionar mientras el rival coopera
    SEVERE_PUNISHMENT = -500 # (S): resultado cuando cooperás y el rival te traiciona
    PUNISHMENT = -250 # (P): penalización cuando ambos se traicionan
    # Para representar el dilema del prisionero: T > R > P > S
    # Condición adicional habitual: 2R > T + S
    
    # Consultar las acciones de ambos jugadores.
    action1 = get_action(player1, history1, history2, score1, score2)
    action2 = get_action(player2, history2, history1, score2, score1)
    if action1 not in ('c', 'b'):
        action1 = ' '
    if action2 not in ('c', 'b'):
        action2 = ' '
    # Agregar las acciones actuales al historial de cada jugador.
    new_history1 = history1 + action1
    new_history2 = history2 + action2
    
    # Actualizar los puntajes según las acciones elegidas.
    if action1 not in ('c','b') or action2 not in ('c','b'):
    # Si alguna acción no es válida, esta ronda no suma ni resta puntos.
        new_score1 = score1
        new_score2 = score2
        
    else: 
    # Las dos estrategias devolvieron acciones válidas.
        if action1 == 'c':
            if action2 == 'c':
                # Ambos cooperan: cada uno recibe la recompensa correspondiente.
                new_score1 = score1 + RELEASE
                new_score2 = score2 + RELEASE
            else:
                # El jugador 1 coopera y el 2 traiciona.
                new_score1 = score1 + SEVERE_PUNISHMENT
                new_score2 = score2 + TREAT
        else:
            if action2 == 'c':
                # El jugador 1 traiciona y el 2 coopera.
                new_score1 = score1 + TREAT
                new_score2 = score2 + SEVERE_PUNISHMENT                       
            else:
                # Ambos traicionan: los dos reciben una penalización.
                new_score1 = score1 + PUNISHMENT
                new_score2 = score2 + PUNISHMENT
                    
    # Devolver los historiales y puntajes actualizados.
    return (new_history1, new_history2, new_score1, new_score2)
   
def play_iterative_rounds(player1, player2):
    """Enfrenta a dos jugadores durante entre 100 y 200 rondas.

    Cada jugador puede consultar lo ocurrido en las rondas anteriores.
    Devuelve el historial de acciones y el puntaje final de cada participante."""
    number_of_rounds = random.randint(100,200)
    moves1 = ''
    moves2 = ''
    score1 = 0
    score2 = 0
    for round in range(number_of_rounds):
        moves1, moves2, score1, score2 = \
            play_round(player1, player2, moves1, moves2, score1, score2)
    return (moves1, moves2, score1, score2)

def get_action(player, history, opponent_history, score, opponent_score, getting_team_name=False):
    """Decide qué acción realiza un jugador en la siguiente ronda.

    'c' significa cooperar y 'b' significa traicionar. Los historiales
    contienen las acciones anteriores, desde la primera hasta la más reciente.
    Si obtener_nombre es True, devuelve el nombre de la estrategia."""
      
    ######
    ######
    #
    # Este jugador de ejemplo siempre coopera.
    if player == 0:
        if getting_team_name:
            return 'Cooperador constante'
        else:
            return 'c'

    
        
            
                
                    
                            
    ######
    ######
    #
    # Este jugador de ejemplo siempre traiciona.
    elif player == 1:
        if getting_team_name:
            return 'Traidor constante'
        else:
            return 'b'








    ######
    ######
    #   
    # Este jugador empieza cooperando y luego responde a una traición.
    # Solo traiciona si en la ronda anterior cooperó y el rival lo traicionó.
    elif player == 2:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival traicionó cuando nosotros cooperamos.
            else:
                return 'c' # En caso contrario, cooperar.


    
    
    
    
    # Cada equipo puede modificar la estrategia de uno de estos bloques elif.










    ######
    ######
    #
    elif player == 3:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.











    ######
    ######
    #
    elif player == 4:
        if getting_team_name:
            return 'Traiciona cada tres rondas'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            size = len(history)
            # Coopera en las rondas 1 y 2; traiciona en cada tercera ronda.
            if (size + 1) % 3 == 0:
                return 'b'
            else:
                return 'c'
    
    
    








    ######
    ######        
    #
    elif player == 5:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    
    
    
    





    ######
    ######        
    #
    elif player == 6:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    










    ######
    ######       
    #
    elif player == 7:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si en la ronda anterior cooperamos y el rival traicionó.
            else:
                return 'c' # En caso contrario, cooperar.











    ######
    ######        
    #
    elif player == 8:
        if getting_team_name:
            # Si ya ocurrió una ronda con las mismas acciones...
            return 'Recuerda patrones anteriores'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar las reglas de esta estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            else:
                # Buscar si ya ocurrió una ronda con las mismas acciones que la última.
                # Si existe, repetir la acción que hizo el rival en la ronda siguiente.
                recent_round_opponent = opponent_history[-1]
                recent_round_me = history[-1]
                            
                # Revisar las rondas anteriores.
                for round in range(len(history)-1):
                    prior_round_opponent = opponent_history[round]
                    prior_round_me = history[round]
                    # Si encontramos una ronda con las mismas acciones...
                    if (prior_round_me == recent_round_me) and \
                            (prior_round_opponent == recent_round_opponent):
                        return opponent_history[round]
                # No se encontró una ronda similar.
                if history[-1]=='c' and opponent_history[-1]=='b':
                    return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
                else:
                    return 'c' # En caso contrario, cooperar.












    ######
    ######
    #
    elif player == 9:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.










    ######
    ######
    #
    elif player == 10:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.









    ######
    ######
    #
    elif player == 11:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.










    ######
    ######
    #
    elif player == 12:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            # La decisión puede basarse en los historiales y los puntajes.
            # Aplicar aquí las reglas de la estrategia.
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    
    


    ######
    ######
    #
    elif player == 13:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    
    







    ######
    ######
    #
    elif player == 14:
        if getting_team_name:
            return 'Coopera con traiciones ocasionales'
        else:
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                if random.random()<0.1: # En el 10 % de las rondas que no cumplen la condición anterior.
                    return 'b'         # Traicionar.
                else:
                    return 'c'         # En caso contrario, cooperar.
    
    
    
    



    ######
    ######
    #
    elif player == 15:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    
    







    ######
    ######
    #
    elif player == 16:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    
    







    ######
    ######
    #
    elif player == 17:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    
    







    ######
    ######
    #
    elif player == 18:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    
    







    ######
    ######
    #
    elif player == 19:
        if getting_team_name:
            return 'Cooperador con respuesta a traiciones'
        else:
            if len(opponent_history)==0: # En la primera ronda, comenzar cooperando.
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # Traicionar si el rival nos perjudicó en la ronda anterior.
            else:
                return 'c' # En caso contrario, cooperar.
    
    







def play_tournament(num_players):
    if not isinstance(num_players, int) or num_players < 1 or num_players > 20:
        raise ValueError('num_players debe ser un entero entre 1 y 20.')
    # Crear un puntaje acumulado para cada jugador.
    scores = []
    for i in range(num_players):
        scores += [0]
    
    
    '''Obtener el nombre de la estrategia de cada jugador.'''
    # Preparar una lista con un espacio para cada jugador.
    team_names = [None] * num_players
    for player in range(num_players):
        team_names[player] = get_action(player,'','',0,0,getting_team_name=True)
             
    # Cada fila y columna representa a un jugador.
    # Inicializar las tablas con el tamaño necesario.
    result_table = [[0.0] * num_players for _ in range(num_players)]
    moves_table = [[" "] * num_players for _ in range(num_players)]
    
    
    for player1 in range(num_players):  
        # Preparar los resultados de este jugador.
        # Inicializar la tabla con una casilla para cada jugador.
        result_table[player1][player1] = 0.0 # La diagonal queda en cero porque un jugador no compite contra sí mismo.
        # Jugar contra cada jugador anterior, evitando repetir enfrentamientos.
        for player2 in range(player1):
            moves1, moves2, score1, score2 = \
                play_iterative_rounds(player1, player2)
            
            rounds = len(moves1)
            score1_per_round = score1/rounds 
            score2_per_round = score2/rounds
            
            result_table[player1][player2]=score1_per_round
            result_table[player2][player1]=score2_per_round
            
            moves_table[player1][player2] = moves1
            moves_table[player2][player1] = moves2
            
            # Acumular el puntaje promedio por ronda de cada participante.
            scores[player1] += score1*1.0/len(moves1)# Se suma el promedio obtenido en este enfrentamiento.
            scores[player2] += score2*1.0/len(moves2)# Se suma el promedio obtenido en este enfrentamiento.
     
    '''Guardar en un archivo los resultados de cada enfrentamiento.'''
    use_datafile=True
    if use_datafile:
        # Guardar el archivo en la misma carpeta que este programa.
        import os.path              
        directory = os.path.dirname(os.path.abspath(__file__))  
        
        # Nombre del archivo que contendrá los resultados.
        filename = os.path.join(directory, 'tournament.txt')
        # Crear el archivo para escribir los resultados.
        results = open(filename, 'w', encoding='utf-8')
        for player1 in range(num_players):
            for player2 in range(player1):
                # Escribir los resultados de este enfrentamiento.
                # Identificar el enfrentamiento por número de jugador.
                results.write('Jugador ' + str(player1) + 
                              ' contra ' + 'Jugador ' + str(player2) +'\n')
                # Mostrar el puntaje promedio por ronda.
                results.write(str(result_table[player1][player2]) + 
                              ' contra ' + str(result_table[player2][player1])+'\n')
                # Mostrar los nombres de las estrategias.
                results.write(team_names[player1] + 
                             ' contra ' + team_names[player2] + '\n')
                # Guardar las acciones de ambos jugadores.
                results.write(moves_table[player1][player2] +'\n')
                results.write(moves_table[player2][player1] +'\n')
                # Dejar una línea en blanco entre enfrentamientos.
                results.write('\n')
            
        # Agregar al final una tabla resumen del torneo.
        # Mostrar el título de la tabla.
        results.write('\n\n\n\tCada columna muestra el puntaje promedio por ronda frente a cada jugador.\n\n\n')
        # Mostrar los encabezados de las columnas.
        results.write('\t') # Dejar vacía la primera columna.
        for player1 in range(num_players):
            results.write('P'+str(player1)+'\t') # Identificar la columna de cada jugador.
        results.write('\n')
        
        # Mostrar los puntajes de cada jugador.
        for player2 in range(num_players):
            results.write('P'+str(player2)+'\t') # Identificar la fila del jugador.
            for player1 in range(num_players):
                # Mostrar el resultado contra cada rival.
                results.write(str(result_table[player1][player2])+'\t') 
            results.write('\n')
        results.write('Total de puntos:\t')
        for player1 in range(num_players):
            results.write(str(int(scores[player1]))+'\t')
        results.write('\n\n\n Promedio por ronda y nombre de cada estrategia:\n\n')       
    
        # Mostrar el número, promedio y nombre de cada estrategia.
        for player in range(num_players):
            results.write('Jugador ' + str(player) + ': ' + \
                    str(scores[player] / (num_players - 1) if num_players > 1 else 0) + ' puntos; estrategia: '+\
                    team_names[player]+'\n')
                    
                    
        # Añadir una copia del código utilizado para generar el torneo.
        results.write('\n\n' + '-'*79 + '\n' + \
                    'Código utilizado para generar estos resultados:\n\n')
        with open(__file__, 'r', encoding='utf-8') as this_code_file:
            for line in this_code_file:
                results.write(line)
        results.close()
                
    '''Mostrar los resultados del torneo en pantalla.'''        
    # Mostrar el título de la tabla.
    print('\n\n\tCada columna muestra el puntaje promedio por ronda frente a cada jugador.\n\n')
    
    # Mostrar los encabezados de las columnas.
    print('\t', end='') # Dejar vacía la primera columna.
    for player1 in range(num_players):
        print('P',player1, end='\t') # Identificar la columna de cada jugador.
    print()
    
    # Mostrar los puntajes de cada jugador.
    for player2 in range(num_players):
        print('P',player2, end='\t') # Identificar la fila del jugador.
        for player1 in range(num_players):
            # Mostrar el resultado contra cada rival.
            print(result_table[player1][player2], end='\t') 
        print()
    # Mostrar la suma de puntos acumulados.
    print('Total de puntos:\t',end='')
    for player1 in range(num_players):
        print(str(int(scores[player1])),end='\t')

    print('\n\n\n Promedio por ronda y nombre de cada estrategia:\n\n')
    # Mostrar el número, promedio y nombre de cada estrategia.
    for player in range(num_players):
        print('Jugador ' + str(player) , ': ' , 
               str(scores[player] / (num_players - 1) if num_players > 1 else 0) , ' puntos; estrategia: ',
               team_names[player])
    

if __name__ == '__main__':
    # El programa contiene las estrategias de los jugadores del 0 al 19. si modificas el 20 por un 30 serian 30 jugadores
    play_tournament(20)
