from transformers import MarianMTModel, MarianTokenizer

# Cargar el modelo y el tokenizador para traducción de inglés a español
model_name = "Helsinki-NLP/opus-mt-en-es"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Frase en inglés a traducir
english_text = "Some jellyfish can be dangerous."

# Tokenizar y traducir la frase
input_ids = tokenizer.encode(english_text, return_tensors="pt")
translated_ids = model.generate(input_ids)
translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)

print("Texto en inglés:", english_text)
print("Traducción al español:", translated_text)