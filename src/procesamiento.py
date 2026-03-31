def score_round(judges):
     return sum(judges.values()) #suma los puntajes de los 3 jueces

def print_round_table(stats):
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)
    
    print("Tabla de posiciones:")
    for rank, (nombre, datos) in enumerate(sorted_stats, 1):
        print(f"  {rank}. {nombre}: {datos['total']} pts")

def print_final_table(stats):
    # Ordenamos igual que antes, por puntaje total
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)
    
    print("\nTabla de posiciones final:")
    # Usamos f-strings con espaciado para alinear las columnas (<15 significa alinear a la izquierda en 15 espacios)
    print(f"{'Cocinero':<15} {'Puntaje':<10} {'Rondas ganadas':<15} {'Mejor ronda':<15} {'Promedio'}")
    print("-" * 70)
    
    for nombre, datos in sorted_stats:
        # Calculamos el promedio
        promedio = datos['total'] / datos['rounds_played']
        
        # Imprimimos la fila con los datos alineados
        print(f"{nombre:<15} {datos['total']:<10} {datos['earned']:<15} {datos['best']:<15} {promedio:.1f}")
    print("-" * 70)

def competition_process(rounds):
    names = rounds[0]['scores'].keys()
    stats = {n: {'total': 0, 'earned': 0, 'best': 0, 'rounds_played': 0} for n in names}

    for i, ronda in enumerate(rounds, 1):
        print(f"\nRonda {i} - {ronda['theme']}:")
        
        puntajes_esta_ronda = {}
        
        for nombre, jueces in ronda['scores'].items():
            puntos = score_round(jueces)
            puntajes_esta_ronda[nombre] = puntos
            
            stats[nombre]['total'] += puntos
            stats[nombre]['rounds_played'] += 1
            if puntos > stats[nombre]['best']:
                stats[nombre]['best'] = puntos
        
        ganador_ronda = max(puntajes_esta_ronda, key=puntajes_esta_ronda.get)
        puntos_ganador = puntajes_esta_ronda[ganador_ronda]
        stats[ganador_ronda]['earned'] += 1
        
        print(f"Ganador: {ganador_ronda} ({puntos_ganador} pts)")
        
        # Llamamos a la función para imprimir la tabla de esta ronda
        print_round_table(stats)
        
    # Al terminar todas las rondas, imprimimos la tabla final
    print_final_table(stats)
    
    return stats