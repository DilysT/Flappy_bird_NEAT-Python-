import pickle
import neat
import json

# Load genome từ file pickle
with open('best.pickle', 'rb') as f:
    best_genome = pickle.load(f)

# Chuyển đổi genome thành dictionary
genome_data = {
    "nodes": list(best_genome.nodes.keys()),  # Danh sách node
    "connections": {
        str(key): {  # Chuyển tuple thành string
            "weight": cg.weight,
            "enabled": cg.enabled
        } for key, cg in best_genome.connections.items()
    }
}

# Lưu vào file JSON
with open("best_genome.json", "w") as f:
    json.dump(genome_data, f, indent=4)

print("✅ Mô hình đã được lưu vào best_genome.json!")
