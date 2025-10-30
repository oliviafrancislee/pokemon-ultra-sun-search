"""
Pokemon Ultra Sun Data Module
Provides Pokemon data for the search application.
"""

import pandas as pd
from typing import Dict, List, Optional


def get_pokemon_data() -> pd.DataFrame:
    """
    Returns static Pokemon data from Pokemon Ultra Sun (Generation 1-7).
    
    Returns:
        pd.DataFrame: DataFrame with columns: name, type1, type2, prev_evolution,
                      next_evolution, hp, attack, defense, sp_attack, sp_defense,
                      speed, total_stats
    """
    # Comprehensive Pokemon data from Gen 1-7 (Pokemon Ultra Sun)
    # This includes a representative sample of Pokemon from each generation
    pokemon_data = [
        # Gen 1 Starters and Evolutions
        {"name": "Bulbasaur", "type1": "Grass", "type2": "Poison", "prev_evolution": None, "next_evolution": "Ivysaur", "hp": 45, "attack": 49, "defense": 49, "sp_attack": 65, "sp_defense": 65, "speed": 45},
        {"name": "Ivysaur", "type1": "Grass", "type2": "Poison", "prev_evolution": "Bulbasaur", "next_evolution": "Venusaur", "hp": 60, "attack": 62, "defense": 63, "sp_attack": 80, "sp_defense": 80, "speed": 60},
        {"name": "Venusaur", "type1": "Grass", "type2": "Poison", "prev_evolution": "Ivysaur", "next_evolution": None, "hp": 80, "attack": 82, "defense": 83, "sp_attack": 100, "sp_defense": 100, "speed": 80},
        {"name": "Charmander", "type1": "Fire", "type2": None, "prev_evolution": None, "next_evolution": "Charmeleon", "hp": 39, "attack": 52, "defense": 43, "sp_attack": 60, "sp_defense": 50, "speed": 65},
        {"name": "Charmeleon", "type1": "Fire", "type2": None, "prev_evolution": "Charmander", "next_evolution": "Charizard", "hp": 58, "attack": 64, "defense": 58, "sp_attack": 80, "sp_defense": 65, "speed": 80},
        {"name": "Charizard", "type1": "Fire", "type2": "Flying", "prev_evolution": "Charmeleon", "next_evolution": None, "hp": 78, "attack": 84, "defense": 78, "sp_attack": 109, "sp_defense": 85, "speed": 100},
        {"name": "Squirtle", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Wartortle", "hp": 44, "attack": 48, "defense": 65, "sp_attack": 50, "sp_defense": 64, "speed": 43},
        {"name": "Wartortle", "type1": "Water", "type2": None, "prev_evolution": "Squirtle", "next_evolution": "Blastoise", "hp": 59, "attack": 63, "defense": 80, "sp_attack": 65, "sp_defense": 80, "speed": 58},
        {"name": "Blastoise", "type1": "Water", "type2": None, "prev_evolution": "Wartortle", "next_evolution": None, "hp": 79, "attack": 83, "defense": 100, "sp_attack": 85, "sp_defense": 105, "speed": 78},
        
        # More Gen 1 Pokemon
        {"name": "Pikachu", "type1": "Electric", "type2": None, "prev_evolution": "Pichu", "next_evolution": "Raichu", "hp": 35, "attack": 55, "defense": 40, "sp_attack": 50, "sp_defense": 50, "speed": 90},
        {"name": "Raichu", "type1": "Electric", "type2": None, "prev_evolution": "Pikachu", "next_evolution": None, "hp": 60, "attack": 90, "defense": 55, "sp_attack": 90, "sp_defense": 80, "speed": 110},
        {"name": "Meowth", "type1": "Normal", "type2": None, "prev_evolution": None, "next_evolution": "Persian", "hp": 40, "attack": 45, "defense": 35, "sp_attack": 40, "sp_defense": 40, "speed": 90},
        {"name": "Persian", "type1": "Normal", "type2": None, "prev_evolution": "Meowth", "next_evolution": None, "hp": 65, "attack": 70, "defense": 60, "sp_attack": 65, "sp_defense": 65, "speed": 115},
        {"name": "Psyduck", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Golduck", "hp": 50, "attack": 52, "defense": 48, "sp_attack": 65, "sp_defense": 50, "speed": 55},
        {"name": "Golduck", "type1": "Water", "type2": None, "prev_evolution": "Psyduck", "next_evolution": None, "hp": 80, "attack": 82, "defense": 78, "sp_attack": 95, "sp_defense": 80, "speed": 85},
        {"name": "Machop", "type1": "Fighting", "type2": None, "prev_evolution": None, "next_evolution": "Machoke", "hp": 70, "attack": 80, "defense": 50, "sp_attack": 35, "sp_defense": 35, "speed": 35},
        {"name": "Machoke", "type1": "Fighting", "type2": None, "prev_evolution": "Machop", "next_evolution": "Machamp", "hp": 80, "attack": 100, "defense": 70, "sp_attack": 50, "sp_defense": 60, "speed": 45},
        {"name": "Machamp", "type1": "Fighting", "type2": None, "prev_evolution": "Machoke", "next_evolution": None, "hp": 90, "attack": 130, "defense": 80, "sp_attack": 65, "sp_defense": 85, "speed": 55},
        {"name": "Geodude", "type1": "Rock", "type2": "Ground", "prev_evolution": None, "next_evolution": "Graveler", "hp": 40, "attack": 80, "defense": 100, "sp_attack": 30, "sp_defense": 30, "speed": 20},
        {"name": "Graveler", "type1": "Rock", "type2": "Ground", "prev_evolution": "Geodude", "next_evolution": "Golem", "hp": 55, "attack": 95, "defense": 115, "sp_attack": 45, "sp_defense": 45, "speed": 35},
        {"name": "Golem", "type1": "Rock", "type2": "Ground", "prev_evolution": "Graveler", "next_evolution": None, "hp": 80, "attack": 120, "defense": 130, "sp_attack": 55, "sp_defense": 65, "speed": 45},
        {"name": "Gastly", "type1": "Ghost", "type2": "Poison", "prev_evolution": None, "next_evolution": "Haunter", "hp": 30, "attack": 35, "defense": 30, "sp_attack": 100, "sp_defense": 35, "speed": 80},
        {"name": "Haunter", "type1": "Ghost", "type2": "Poison", "prev_evolution": "Gastly", "next_evolution": "Gengar", "hp": 45, "attack": 50, "defense": 45, "sp_attack": 115, "sp_defense": 55, "speed": 95},
        {"name": "Gengar", "type1": "Ghost", "type2": "Poison", "prev_evolution": "Haunter", "next_evolution": None, "hp": 60, "attack": 65, "defense": 60, "sp_attack": 130, "sp_defense": 75, "speed": 110},
        {"name": "Magikarp", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Gyarados", "hp": 20, "attack": 10, "defense": 55, "sp_attack": 15, "sp_defense": 20, "speed": 80},
        {"name": "Gyarados", "type1": "Water", "type2": "Flying", "prev_evolution": "Magikarp", "next_evolution": None, "hp": 95, "attack": 125, "defense": 79, "sp_attack": 60, "sp_defense": 100, "speed": 81},
        {"name": "Eevee", "type1": "Normal", "type2": None, "prev_evolution": None, "next_evolution": "Vaporeon", "hp": 55, "attack": 55, "defense": 50, "sp_attack": 45, "sp_defense": 65, "speed": 55},
        {"name": "Vaporeon", "type1": "Water", "type2": None, "prev_evolution": "Eevee", "next_evolution": None, "hp": 130, "attack": 65, "defense": 60, "sp_attack": 110, "sp_defense": 95, "speed": 65},
        {"name": "Jolteon", "type1": "Electric", "type2": None, "prev_evolution": "Eevee", "next_evolution": None, "hp": 65, "attack": 65, "defense": 60, "sp_attack": 110, "sp_defense": 95, "speed": 130},
        {"name": "Flareon", "type1": "Fire", "type2": None, "prev_evolution": "Eevee", "next_evolution": None, "hp": 65, "attack": 130, "defense": 60, "sp_attack": 95, "sp_defense": 110, "speed": 65},
        {"name": "Dratini", "type1": "Dragon", "type2": None, "prev_evolution": None, "next_evolution": "Dragonair", "hp": 41, "attack": 64, "defense": 45, "sp_attack": 50, "sp_defense": 50, "speed": 50},
        {"name": "Dragonair", "type1": "Dragon", "type2": None, "prev_evolution": "Dratini", "next_evolution": "Dragonite", "hp": 61, "attack": 84, "defense": 65, "sp_attack": 70, "sp_defense": 70, "speed": 70},
        {"name": "Dragonite", "type1": "Dragon", "type2": "Flying", "prev_evolution": "Dragonair", "next_evolution": None, "hp": 91, "attack": 134, "defense": 95, "sp_attack": 100, "sp_defense": 100, "speed": 80},
        {"name": "Mewtwo", "type1": "Psychic", "type2": None, "prev_evolution": None, "next_evolution": None, "hp": 106, "attack": 110, "defense": 90, "sp_attack": 154, "sp_defense": 90, "speed": 130},
        {"name": "Mew", "type1": "Psychic", "type2": None, "prev_evolution": None, "next_evolution": None, "hp": 100, "attack": 100, "defense": 100, "sp_attack": 100, "sp_defense": 100, "speed": 100},
        
        # Gen 2 Pokemon
        {"name": "Chikorita", "type1": "Grass", "type2": None, "prev_evolution": None, "next_evolution": "Bayleef", "hp": 45, "attack": 49, "defense": 65, "sp_attack": 49, "sp_defense": 65, "speed": 45},
        {"name": "Bayleef", "type1": "Grass", "type2": None, "prev_evolution": "Chikorita", "next_evolution": "Meganium", "hp": 60, "attack": 62, "defense": 80, "sp_attack": 63, "sp_defense": 80, "speed": 60},
        {"name": "Meganium", "type1": "Grass", "type2": None, "prev_evolution": "Bayleef", "next_evolution": None, "hp": 80, "attack": 82, "defense": 100, "sp_attack": 83, "sp_defense": 100, "speed": 80},
        {"name": "Cyndaquil", "type1": "Fire", "type2": None, "prev_evolution": None, "next_evolution": "Quilava", "hp": 39, "attack": 52, "defense": 43, "sp_attack": 60, "sp_defense": 50, "speed": 65},
        {"name": "Quilava", "type1": "Fire", "type2": None, "prev_evolution": "Cyndaquil", "next_evolution": "Typhlosion", "hp": 58, "attack": 64, "defense": 58, "sp_attack": 80, "sp_defense": 65, "speed": 80},
        {"name": "Typhlosion", "type1": "Fire", "type2": None, "prev_evolution": "Quilava", "next_evolution": None, "hp": 78, "attack": 84, "defense": 78, "sp_attack": 109, "sp_defense": 85, "speed": 100},
        {"name": "Totodile", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Croconaw", "hp": 50, "attack": 65, "defense": 64, "sp_attack": 44, "sp_defense": 48, "speed": 43},
        {"name": "Croconaw", "type1": "Water", "type2": None, "prev_evolution": "Totodile", "next_evolution": "Feraligatr", "hp": 65, "attack": 80, "defense": 80, "sp_attack": 59, "sp_defense": 63, "speed": 58},
        {"name": "Feraligatr", "type1": "Water", "type2": None, "prev_evolution": "Croconaw", "next_evolution": None, "hp": 85, "attack": 105, "defense": 100, "sp_attack": 79, "sp_defense": 83, "speed": 78},
        {"name": "Pichu", "type1": "Electric", "type2": None, "prev_evolution": None, "next_evolution": "Pikachu", "hp": 20, "attack": 40, "defense": 15, "sp_attack": 35, "sp_defense": 35, "speed": 60},
        {"name": "Togepi", "type1": "Fairy", "type2": None, "prev_evolution": None, "next_evolution": "Togetic", "hp": 35, "attack": 20, "defense": 65, "sp_attack": 40, "sp_defense": 65, "speed": 20},
        {"name": "Togetic", "type1": "Fairy", "type2": "Flying", "prev_evolution": "Togepi", "next_evolution": "Togekiss", "hp": 55, "attack": 40, "defense": 85, "sp_attack": 80, "sp_defense": 105, "speed": 40},
        {"name": "Mareep", "type1": "Electric", "type2": None, "prev_evolution": None, "next_evolution": "Flaaffy", "hp": 55, "attack": 40, "defense": 40, "sp_attack": 65, "sp_defense": 45, "speed": 35},
        {"name": "Flaaffy", "type1": "Electric", "type2": None, "prev_evolution": "Mareep", "next_evolution": "Ampharos", "hp": 70, "attack": 55, "defense": 55, "sp_attack": 80, "sp_defense": 60, "speed": 45},
        {"name": "Ampharos", "type1": "Electric", "type2": None, "prev_evolution": "Flaaffy", "next_evolution": None, "hp": 90, "attack": 75, "defense": 85, "sp_attack": 115, "sp_defense": 90, "speed": 55},
        {"name": "Espeon", "type1": "Psychic", "type2": None, "prev_evolution": "Eevee", "next_evolution": None, "hp": 65, "attack": 65, "defense": 60, "sp_attack": 130, "sp_defense": 95, "speed": 110},
        {"name": "Umbreon", "type1": "Dark", "type2": None, "prev_evolution": "Eevee", "next_evolution": None, "hp": 95, "attack": 65, "defense": 110, "sp_attack": 60, "sp_defense": 130, "speed": 65},
        {"name": "Tyranitar", "type1": "Rock", "type2": "Dark", "prev_evolution": "Pupitar", "next_evolution": None, "hp": 100, "attack": 134, "defense": 110, "sp_attack": 95, "sp_defense": 100, "speed": 61},
        {"name": "Lugia", "type1": "Psychic", "type2": "Flying", "prev_evolution": None, "next_evolution": None, "hp": 106, "attack": 90, "defense": 130, "sp_attack": 90, "sp_defense": 154, "speed": 110},
        {"name": "Ho Oh", "type1": "Fire", "type2": "Flying", "prev_evolution": None, "next_evolution": None, "hp": 106, "attack": 130, "defense": 90, "sp_attack": 110, "sp_defense": 154, "speed": 90},
        
        # Gen 3 Pokemon
        {"name": "Treecko", "type1": "Grass", "type2": None, "prev_evolution": None, "next_evolution": "Grovyle", "hp": 40, "attack": 45, "defense": 35, "sp_attack": 65, "sp_defense": 55, "speed": 70},
        {"name": "Grovyle", "type1": "Grass", "type2": None, "prev_evolution": "Treecko", "next_evolution": "Sceptile", "hp": 50, "attack": 65, "defense": 45, "sp_attack": 85, "sp_defense": 65, "speed": 95},
        {"name": "Sceptile", "type1": "Grass", "type2": None, "prev_evolution": "Grovyle", "next_evolution": None, "hp": 70, "attack": 85, "defense": 65, "sp_attack": 105, "sp_defense": 85, "speed": 120},
        {"name": "Torchic", "type1": "Fire", "type2": None, "prev_evolution": None, "next_evolution": "Combusken", "hp": 45, "attack": 60, "defense": 40, "sp_attack": 70, "sp_defense": 50, "speed": 45},
        {"name": "Combusken", "type1": "Fire", "type2": "Fighting", "prev_evolution": "Torchic", "next_evolution": "Blaziken", "hp": 60, "attack": 85, "defense": 60, "sp_attack": 85, "sp_defense": 60, "speed": 55},
        {"name": "Blaziken", "type1": "Fire", "type2": "Fighting", "prev_evolution": "Combusken", "next_evolution": None, "hp": 80, "attack": 120, "defense": 70, "sp_attack": 110, "sp_defense": 70, "speed": 80},
        {"name": "Mudkip", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Marshtomp", "hp": 50, "attack": 70, "defense": 50, "sp_attack": 50, "sp_defense": 50, "speed": 40},
        {"name": "Marshtomp", "type1": "Water", "type2": "Ground", "prev_evolution": "Mudkip", "next_evolution": "Swampert", "hp": 70, "attack": 85, "defense": 70, "sp_attack": 60, "sp_defense": 70, "speed": 50},
        {"name": "Swampert", "type1": "Water", "type2": "Ground", "prev_evolution": "Marshtomp", "next_evolution": None, "hp": 100, "attack": 110, "defense": 90, "sp_attack": 85, "sp_defense": 90, "speed": 60},
        {"name": "Ralts", "type1": "Psychic", "type2": "Fairy", "prev_evolution": None, "next_evolution": "Kirlia", "hp": 28, "attack": 25, "defense": 25, "sp_attack": 45, "sp_defense": 35, "speed": 40},
        {"name": "Kirlia", "type1": "Psychic", "type2": "Fairy", "prev_evolution": "Ralts", "next_evolution": "Gardevoir", "hp": 38, "attack": 35, "defense": 35, "sp_attack": 65, "sp_defense": 55, "speed": 50},
        {"name": "Gardevoir", "type1": "Psychic", "type2": "Fairy", "prev_evolution": "Kirlia", "next_evolution": None, "hp": 68, "attack": 65, "defense": 65, "sp_attack": 125, "sp_defense": 115, "speed": 80},
        {"name": "Aggron", "type1": "Steel", "type2": "Rock", "prev_evolution": "Lairon", "next_evolution": None, "hp": 70, "attack": 110, "defense": 180, "sp_attack": 60, "sp_defense": 60, "speed": 50},
        {"name": "Flygon", "type1": "Ground", "type2": "Dragon", "prev_evolution": "Vibrava", "next_evolution": None, "hp": 80, "attack": 100, "defense": 80, "sp_attack": 80, "sp_defense": 80, "speed": 100},
        {"name": "Metagross", "type1": "Steel", "type2": "Psychic", "prev_evolution": "Metang", "next_evolution": None, "hp": 80, "attack": 135, "defense": 130, "sp_attack": 95, "sp_defense": 90, "speed": 70},
        {"name": "Rayquaza", "type1": "Dragon", "type2": "Flying", "prev_evolution": None, "next_evolution": None, "hp": 105, "attack": 150, "defense": 90, "sp_attack": 150, "sp_defense": 90, "speed": 95},
        {"name": "Kyogre", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": None, "hp": 100, "attack": 100, "defense": 90, "sp_attack": 150, "sp_defense": 140, "speed": 90},
        {"name": "Groudon", "type1": "Ground", "type2": None, "prev_evolution": None, "next_evolution": None, "hp": 100, "attack": 150, "defense": 140, "sp_attack": 100, "sp_defense": 90, "speed": 90},
        
        # Gen 4 Pokemon
        {"name": "Turtwig", "type1": "Grass", "type2": None, "prev_evolution": None, "next_evolution": "Grotle", "hp": 55, "attack": 68, "defense": 64, "sp_attack": 45, "sp_defense": 55, "speed": 31},
        {"name": "Grotle", "type1": "Grass", "type2": None, "prev_evolution": "Turtwig", "next_evolution": "Torterra", "hp": 75, "attack": 89, "defense": 85, "sp_attack": 55, "sp_defense": 65, "speed": 36},
        {"name": "Torterra", "type1": "Grass", "type2": "Ground", "prev_evolution": "Grotle", "next_evolution": None, "hp": 95, "attack": 109, "defense": 105, "sp_attack": 75, "sp_defense": 85, "speed": 56},
        {"name": "Chimchar", "type1": "Fire", "type2": None, "prev_evolution": None, "next_evolution": "Monferno", "hp": 44, "attack": 58, "defense": 44, "sp_attack": 58, "sp_defense": 44, "speed": 61},
        {"name": "Monferno", "type1": "Fire", "type2": "Fighting", "prev_evolution": "Chimchar", "next_evolution": "Infernape", "hp": 64, "attack": 78, "defense": 52, "sp_attack": 78, "sp_defense": 52, "speed": 81},
        {"name": "Infernape", "type1": "Fire", "type2": "Fighting", "prev_evolution": "Monferno", "next_evolution": None, "hp": 76, "attack": 104, "defense": 71, "sp_attack": 104, "sp_defense": 71, "speed": 108},
        {"name": "Piplup", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Prinplup", "hp": 53, "attack": 51, "defense": 53, "sp_attack": 61, "sp_defense": 56, "speed": 40},
        {"name": "Prinplup", "type1": "Water", "type2": None, "prev_evolution": "Piplup", "next_evolution": "Empoleon", "hp": 64, "attack": 66, "defense": 68, "sp_attack": 81, "sp_defense": 76, "speed": 50},
        {"name": "Empoleon", "type1": "Water", "type2": "Steel", "prev_evolution": "Prinplup", "next_evolution": None, "hp": 84, "attack": 86, "defense": 88, "sp_attack": 111, "sp_defense": 101, "speed": 60},
        {"name": "Luxray", "type1": "Electric", "type2": None, "prev_evolution": "Luxio", "next_evolution": None, "hp": 80, "attack": 120, "defense": 79, "sp_attack": 95, "sp_defense": 79, "speed": 70},
        {"name": "Garchomp", "type1": "Dragon", "type2": "Ground", "prev_evolution": "Gabite", "next_evolution": None, "hp": 108, "attack": 130, "defense": 95, "sp_attack": 80, "sp_defense": 85, "speed": 102},
        {"name": "Lucario", "type1": "Fighting", "type2": "Steel", "prev_evolution": "Riolu", "next_evolution": None, "hp": 70, "attack": 110, "defense": 70, "sp_attack": 115, "sp_defense": 70, "speed": 90},
        {"name": "Leafeon", "type1": "Grass", "type2": None, "prev_evolution": "Eevee", "next_evolution": None, "hp": 65, "attack": 110, "defense": 130, "sp_attack": 60, "sp_defense": 65, "speed": 95},
        {"name": "Glaceon", "type1": "Ice", "type2": None, "prev_evolution": "Eevee", "next_evolution": None, "hp": 65, "attack": 60, "defense": 110, "sp_attack": 130, "sp_defense": 95, "speed": 65},
        {"name": "Togekiss", "type1": "Fairy", "type2": "Flying", "prev_evolution": "Togetic", "next_evolution": None, "hp": 85, "attack": 50, "defense": 95, "sp_attack": 120, "sp_defense": 115, "speed": 80},
        {"name": "Dialga", "type1": "Steel", "type2": "Dragon", "prev_evolution": None, "next_evolution": None, "hp": 100, "attack": 120, "defense": 120, "sp_attack": 150, "sp_defense": 100, "speed": 90},
        {"name": "Palkia", "type1": "Water", "type2": "Dragon", "prev_evolution": None, "next_evolution": None, "hp": 90, "attack": 120, "defense": 100, "sp_attack": 150, "sp_defense": 120, "speed": 100},
        {"name": "Giratina", "type1": "Ghost", "type2": "Dragon", "prev_evolution": None, "next_evolution": None, "hp": 150, "attack": 100, "defense": 120, "sp_attack": 100, "sp_defense": 120, "speed": 90},
        {"name": "Arceus", "type1": "Normal", "type2": None, "prev_evolution": None, "next_evolution": None, "hp": 120, "attack": 120, "defense": 120, "sp_attack": 120, "sp_defense": 120, "speed": 120},
        
        # Gen 5 Pokemon
        {"name": "Snivy", "type1": "Grass", "type2": None, "prev_evolution": None, "next_evolution": "Servine", "hp": 45, "attack": 45, "defense": 55, "sp_attack": 45, "sp_defense": 55, "speed": 63},
        {"name": "Servine", "type1": "Grass", "type2": None, "prev_evolution": "Snivy", "next_evolution": "Serperior", "hp": 60, "attack": 60, "defense": 75, "sp_attack": 60, "sp_defense": 75, "speed": 83},
        {"name": "Serperior", "type1": "Grass", "type2": None, "prev_evolution": "Servine", "next_evolution": None, "hp": 75, "attack": 75, "defense": 95, "sp_attack": 75, "sp_defense": 95, "speed": 113},
        {"name": "Tepig", "type1": "Fire", "type2": None, "prev_evolution": None, "next_evolution": "Pignite", "hp": 65, "attack": 63, "defense": 45, "sp_attack": 45, "sp_defense": 45, "speed": 45},
        {"name": "Pignite", "type1": "Fire", "type2": "Fighting", "prev_evolution": "Tepig", "next_evolution": "Emboar", "hp": 90, "attack": 93, "defense": 55, "sp_attack": 70, "sp_defense": 55, "speed": 55},
        {"name": "Emboar", "type1": "Fire", "type2": "Fighting", "prev_evolution": "Pignite", "next_evolution": None, "hp": 110, "attack": 123, "defense": 65, "sp_attack": 100, "sp_defense": 65, "speed": 65},
        {"name": "Oshawott", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Dewott", "hp": 55, "attack": 55, "defense": 45, "sp_attack": 63, "sp_defense": 45, "speed": 45},
        {"name": "Dewott", "type1": "Water", "type2": None, "prev_evolution": "Oshawott", "next_evolution": "Samurott", "hp": 75, "attack": 75, "defense": 60, "sp_attack": 83, "sp_defense": 60, "speed": 60},
        {"name": "Samurott", "type1": "Water", "type2": None, "prev_evolution": "Dewott", "next_evolution": None, "hp": 95, "attack": 100, "defense": 85, "sp_attack": 108, "sp_defense": 70, "speed": 70},
        {"name": "Zoroark", "type1": "Dark", "type2": None, "prev_evolution": "Zorua", "next_evolution": None, "hp": 60, "attack": 105, "defense": 60, "sp_attack": 120, "sp_defense": 60, "speed": 105},
        {"name": "Hydreigon", "type1": "Dark", "type2": "Dragon", "prev_evolution": "Zweilous", "next_evolution": None, "hp": 92, "attack": 105, "defense": 90, "sp_attack": 125, "sp_defense": 90, "speed": 98},
        {"name": "Reshiram", "type1": "Dragon", "type2": "Fire", "prev_evolution": None, "next_evolution": None, "hp": 100, "attack": 120, "defense": 100, "sp_attack": 150, "sp_defense": 120, "speed": 90},
        {"name": "Zekrom", "type1": "Dragon", "type2": "Electric", "prev_evolution": None, "next_evolution": None, "hp": 100, "attack": 150, "defense": 120, "sp_attack": 120, "sp_defense": 100, "speed": 90},
        {"name": "Kyurem", "type1": "Dragon", "type2": "Ice", "prev_evolution": None, "next_evolution": None, "hp": 125, "attack": 130, "defense": 90, "sp_attack": 130, "sp_defense": 90, "speed": 95},
        
        # Gen 6 Pokemon
        {"name": "Chespin", "type1": "Grass", "type2": None, "prev_evolution": None, "next_evolution": "Quilladin", "hp": 56, "attack": 61, "defense": 65, "sp_attack": 48, "sp_defense": 45, "speed": 38},
        {"name": "Quilladin", "type1": "Grass", "type2": None, "prev_evolution": "Chespin", "next_evolution": "Chesnaught", "hp": 61, "attack": 78, "defense": 95, "sp_attack": 56, "sp_defense": 58, "speed": 57},
        {"name": "Chesnaught", "type1": "Grass", "type2": "Fighting", "prev_evolution": "Quilladin", "next_evolution": None, "hp": 88, "attack": 107, "defense": 122, "sp_attack": 74, "sp_defense": 75, "speed": 64},
        {"name": "Fennekin", "type1": "Fire", "type2": None, "prev_evolution": None, "next_evolution": "Braixen", "hp": 40, "attack": 45, "defense": 40, "sp_attack": 62, "sp_defense": 60, "speed": 60},
        {"name": "Braixen", "type1": "Fire", "type2": None, "prev_evolution": "Fennekin", "next_evolution": "Delphox", "hp": 59, "attack": 59, "defense": 58, "sp_attack": 90, "sp_defense": 70, "speed": 73},
        {"name": "Delphox", "type1": "Fire", "type2": "Psychic", "prev_evolution": "Braixen", "next_evolution": None, "hp": 75, "attack": 69, "defense": 72, "sp_attack": 114, "sp_defense": 100, "speed": 104},
        {"name": "Froakie", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Frogadier", "hp": 41, "attack": 56, "defense": 40, "sp_attack": 62, "sp_defense": 44, "speed": 71},
        {"name": "Frogadier", "type1": "Water", "type2": None, "prev_evolution": "Froakie", "next_evolution": "Greninja", "hp": 54, "attack": 63, "defense": 52, "sp_attack": 83, "sp_defense": 56, "speed": 97},
        {"name": "Greninja", "type1": "Water", "type2": "Dark", "prev_evolution": "Frogadier", "next_evolution": None, "hp": 72, "attack": 95, "defense": 67, "sp_attack": 103, "sp_defense": 71, "speed": 122},
        {"name": "Sylveon", "type1": "Fairy", "type2": None, "prev_evolution": "Eevee", "next_evolution": None, "hp": 95, "attack": 65, "defense": 65, "sp_attack": 110, "sp_defense": 130, "speed": 60},
        {"name": "Goodra", "type1": "Dragon", "type2": None, "prev_evolution": "Sliggoo", "next_evolution": None, "hp": 90, "attack": 100, "defense": 70, "sp_attack": 110, "sp_defense": 150, "speed": 80},
        {"name": "Xerneas", "type1": "Fairy", "type2": None, "prev_evolution": None, "next_evolution": None, "hp": 126, "attack": 131, "defense": 95, "sp_attack": 131, "sp_defense": 98, "speed": 99},
        {"name": "Yveltal", "type1": "Dark", "type2": "Flying", "prev_evolution": None, "next_evolution": None, "hp": 126, "attack": 131, "defense": 95, "sp_attack": 131, "sp_defense": 98, "speed": 99},
        
        # Gen 7 Pokemon (Alola)
        {"name": "Rowlet", "type1": "Grass", "type2": "Flying", "prev_evolution": None, "next_evolution": "Dartrix", "hp": 68, "attack": 55, "defense": 55, "sp_attack": 50, "sp_defense": 50, "speed": 42},
        {"name": "Dartrix", "type1": "Grass", "type2": "Flying", "prev_evolution": "Rowlet", "next_evolution": "Decidueye", "hp": 78, "attack": 75, "defense": 75, "sp_attack": 70, "sp_defense": 70, "speed": 52},
        {"name": "Decidueye", "type1": "Grass", "type2": "Ghost", "prev_evolution": "Dartrix", "next_evolution": None, "hp": 78, "attack": 107, "defense": 75, "sp_attack": 100, "sp_defense": 100, "speed": 70},
        {"name": "Litten", "type1": "Fire", "type2": None, "prev_evolution": None, "next_evolution": "Torracat", "hp": 45, "attack": 65, "defense": 40, "sp_attack": 60, "sp_defense": 40, "speed": 70},
        {"name": "Torracat", "type1": "Fire", "type2": None, "prev_evolution": "Litten", "next_evolution": "Incineroar", "hp": 65, "attack": 85, "defense": 50, "sp_attack": 80, "sp_defense": 50, "speed": 90},
        {"name": "Incineroar", "type1": "Fire", "type2": "Dark", "prev_evolution": "Torracat", "next_evolution": None, "hp": 95, "attack": 115, "defense": 90, "sp_attack": 80, "sp_defense": 90, "speed": 60},
        {"name": "Popplio", "type1": "Water", "type2": None, "prev_evolution": None, "next_evolution": "Brionne", "hp": 50, "attack": 54, "defense": 54, "sp_attack": 66, "sp_defense": 56, "speed": 40},
        {"name": "Brionne", "type1": "Water", "type2": None, "prev_evolution": "Popplio", "next_evolution": "Primarina", "hp": 60, "attack": 69, "defense": 69, "sp_attack": 91, "sp_defense": 81, "speed": 50},
        {"name": "Primarina", "type1": "Water", "type2": "Fairy", "prev_evolution": "Brionne", "next_evolution": None, "hp": 80, "attack": 74, "defense": 74, "sp_attack": 126, "sp_defense": 116, "speed": 60},
        {"name": "Lycanroc", "type1": "Rock", "type2": None, "prev_evolution": "Rockruff", "next_evolution": None, "hp": 75, "attack": 115, "defense": 65, "sp_attack": 55, "sp_defense": 65, "speed": 112},
        {"name": "Mimikyu", "type1": "Ghost", "type2": "Fairy", "prev_evolution": None, "next_evolution": None, "hp": 55, "attack": 90, "defense": 80, "sp_attack": 50, "sp_defense": 105, "speed": 96},
        {"name": "Kommo O", "type1": "Dragon", "type2": "Fighting", "prev_evolution": "Hakamo O", "next_evolution": None, "hp": 75, "attack": 110, "defense": 125, "sp_attack": 100, "sp_defense": 105, "speed": 85},
        {"name": "Solgaleo", "type1": "Psychic", "type2": "Steel", "prev_evolution": "Cosmoem", "next_evolution": None, "hp": 137, "attack": 137, "defense": 107, "sp_attack": 113, "sp_defense": 89, "speed": 97},
        {"name": "Lunala", "type1": "Psychic", "type2": "Ghost", "prev_evolution": "Cosmoem", "next_evolution": None, "hp": 137, "attack": 113, "defense": 89, "sp_attack": 137, "sp_defense": 107, "speed": 97},
        {"name": "Necrozma", "type1": "Psychic", "type2": None, "prev_evolution": None, "next_evolution": None, "hp": 97, "attack": 107, "defense": 101, "sp_attack": 127, "sp_defense": 89, "speed": 79},
        
        # Additional popular Pokemon
        {"name": "Alakazam", "type1": "Psychic", "type2": None, "prev_evolution": "Kadabra", "next_evolution": None, "hp": 55, "attack": 50, "defense": 45, "sp_attack": 135, "sp_defense": 95, "speed": 120},
        {"name": "Slowbro", "type1": "Water", "type2": "Psychic", "prev_evolution": "Slowpoke", "next_evolution": None, "hp": 95, "attack": 75, "defense": 110, "sp_attack": 100, "sp_defense": 80, "speed": 30},
        {"name": "Lapras", "type1": "Water", "type2": "Ice", "prev_evolution": None, "next_evolution": None, "hp": 130, "attack": 85, "defense": 80, "sp_attack": 85, "sp_defense": 95, "speed": 60},
        {"name": "Snorlax", "type1": "Normal", "type2": None, "prev_evolution": "Munchlax", "next_evolution": None, "hp": 160, "attack": 110, "defense": 65, "sp_attack": 65, "sp_defense": 110, "speed": 30},
        {"name": "Articuno", "type1": "Ice", "type2": "Flying", "prev_evolution": None, "next_evolution": None, "hp": 90, "attack": 85, "defense": 100, "sp_attack": 95, "sp_defense": 125, "speed": 85},
        {"name": "Zapdos", "type1": "Electric", "type2": "Flying", "prev_evolution": None, "next_evolution": None, "hp": 90, "attack": 90, "defense": 85, "sp_attack": 125, "sp_defense": 90, "speed": 100},
        {"name": "Moltres", "type1": "Fire", "type2": "Flying", "prev_evolution": None, "next_evolution": None, "hp": 90, "attack": 100, "defense": 90, "sp_attack": 125, "sp_defense": 85, "speed": 90},
        {"name": "Scizor", "type1": "Bug", "type2": "Steel", "prev_evolution": "Scyther", "next_evolution": None, "hp": 70, "attack": 130, "defense": 100, "sp_attack": 55, "sp_defense": 80, "speed": 65},
        {"name": "Heracross", "type1": "Bug", "type2": "Fighting", "prev_evolution": None, "next_evolution": None, "hp": 80, "attack": 125, "defense": 75, "sp_attack": 40, "sp_defense": 95, "speed": 85},
        {"name": "Kingdra", "type1": "Water", "type2": "Dragon", "prev_evolution": "Seadra", "next_evolution": None, "hp": 75, "attack": 95, "defense": 95, "sp_attack": 95, "sp_defense": 95, "speed": 85},
        {"name": "Milotic", "type1": "Water", "type2": None, "prev_evolution": "Feebas", "next_evolution": None, "hp": 95, "attack": 60, "defense": 79, "sp_attack": 100, "sp_defense": 125, "speed": 81},
        {"name": "Salamence", "type1": "Dragon", "type2": "Flying", "prev_evolution": "Shelgon", "next_evolution": None, "hp": 95, "attack": 135, "defense": 80, "sp_attack": 110, "sp_defense": 80, "speed": 100},
        {"name": "Breloom", "type1": "Grass", "type2": "Fighting", "prev_evolution": "Shroomish", "next_evolution": None, "hp": 60, "attack": 130, "defense": 80, "sp_attack": 60, "sp_defense": 60, "speed": 70},
        {"name": "Slaking", "type1": "Normal", "type2": None, "prev_evolution": "Vigoroth", "next_evolution": None, "hp": 150, "attack": 160, "defense": 100, "sp_attack": 95, "sp_defense": 65, "speed": 100},
        {"name": "Absol", "type1": "Dark", "type2": None, "prev_evolution": None, "next_evolution": None, "hp": 65, "attack": 130, "defense": 60, "sp_attack": 75, "sp_defense": 60, "speed": 75},
    ]
    
    # Create DataFrame
    df = pd.DataFrame(pokemon_data)
    
    # Calculate total stats
    df['total_stats'] = df['hp'] + df['attack'] + df['defense'] + df['sp_attack'] + df['sp_defense'] + df['speed']
    
    return df


if __name__ == "__main__":
    df = get_pokemon_data()
    print("\nSample data:")
    print(df.head(10))
    print(f"\nTotal Pokemon: {len(df)}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nTotal Stats Range: {df['total_stats'].min()} - {df['total_stats'].max()}")
    print(f"\nTypes available: {sorted(set(df['type1'].dropna()) | set(df['type2'].dropna()))}")
