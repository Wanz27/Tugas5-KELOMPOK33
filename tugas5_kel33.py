class Quiz:
    def __init__(self):
        self.points = 0
    
    def participate_quiz(self, name, age):
        if not isinstance(age, int):
            print("Error! Masukkan usia dalam bentuk angka.")
            return
        
if age >= 18:
            print(f"Selamat, {name}! Anda bisa ikut kuis.")
            print("Jawablah pertanyaan berikut ini:")
            self.ask_question("Berapa hasil dari 12/2?", "6")
            self.ask_question("Berapa hasil dari 10 + 5?", "15")
            self.ask_question("Berapa hasil dari 26 - 15?", "11")
            self.ask_question("Berapa hasil dari 8 x 5?", "40")
            self.ask_question("Berapa hasil dari 7 x 3?", "21")
            print(f"Total poin Anda: {self.points}")
        else:
            print("Maaf, Anda belum cukup umur untuk ikut kuis.")        


































