import os
import time
import csv

if __name__ == "__main__":
    
    last_update = os.path.getmtime('birdTracker.birds.csv')
    
    while True:
        
        current_update = os.path.getmtime('birdTracker.birds.csv')
        if current_update != last_update:
    
            total_sightings = 0
            species_dict = {} 
            
            with open("birdTracker.birds.csv", 'r') as file:
                reader = csv.DictReader(file)
                for line in reader:
                    total_sightings += 1
                    species = line['species']
                    if species not in species_dict:
                        species_dict[species] = 1
                    else:
                        species_dict[species] += 1
            
            max_sightings = max(species_dict.values())
            max_sightings_species = [item[0] for item in species_dict.items() if item[1] == max_sightings]

            with open("OutputFile.txt", 'w') as file:
                for species in max_sightings_species:
                    file.write(str((total_sightings, species, max_sightings)) + '\n')

            last_update = current_update
        time.sleep(5)
