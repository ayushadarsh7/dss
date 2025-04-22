import pickle
import random
import os
import math

with open("Dominant_Categories.pkl", "rb") as f:
    Dominant_Categories = pickle.load(f)

with open("dominant_categories_list_reco_grop_size_5_reco_5", "rb") as f:
    dominant_categories_list_reco_grop_size_5_reco_5 = pickle.load(f)

with open("dominant_categories_list_reco_grop_size_5_reco_10", "rb") as f:
    dominant_categories_list_reco_grop_size_5_reco_10 = pickle.load(f)

with open("dominant_categories_of_each_group_size_5.pkl", "rb") as f:
    dominant_categories_of_each_group_size_5 = pickle.load(f)

with open("group_vectors_size_5.pkl", "rb") as f:
    group_vectors = pickle.load(f)

Dominant_Categories = [ele.capitalize() for ele in Dominant_Categories]

category_to_index = {cat: idx for idx, cat in enumerate(Dominant_Categories)}

def list_to_frequency_vector(category_list, category_to_index, vector_size=122):
    freq_vector = [0] * vector_size

    for ele in category_list:
        ele = ele.capitalize()
        if ele in category_to_index:
            idx = category_to_index[ele]
            freq_vector[idx] += 1

    return freq_vector

def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    if norm1 == 0 or norm2 == 0:
        return 0
    return dot / (norm1 * norm2)

def find_most_similar_group(input_vector, group_vectors):
    max_sim = -1
    best_match = None

    for idx, group_vec in group_vectors.items():
        sim = cosine_similarity(input_vector, group_vec)
        if sim > max_sim:
            max_sim = sim
            best_match = idx

    return best_match, max_sim

user_1 = ['Mexican', 'Chinese', 'Chinese', 'American', 'Chinese']
user_2 = ["Bars", "Bars", "Buffets", "Bars", "Diners"]
user_3 = ["Pizza", "Burgers", "Barbeque"]
user_4 = ["Pizza", "Noodles", "Vegetarian"]
user_5 = [ "Vegan", "Vegan", "Vegan", "Vegan"]

A = user_1 + user_2 + user_3 + user_4 + user_5


vec = list_to_frequency_vector(A, category_to_index, vector_size=122)
(best_group, sim) = find_most_similar_group(vec, group_vectors)



def get_recommendations(best_group):
    return dominant_categories_list_reco_grop_size_5_reco_5[best_group]

recom = get_recommendations(best_group)

for k, v in recom.items():
    print(k, v)
