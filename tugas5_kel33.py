class Quiz:
    def __init__(self):
        self.points = 0
    
    def participate_quiz(self, name, age):
        if not isinstance(age, int):
            print("Error! Masukkan usia dalam bentuk angka.")
            return
        
        if age >= 18:
            print(f"Selamat, {name}! Anda bisa ikut kuis.")
            while True:
                self.ask_question("Berapa hasil dari 12/2?", "6")
                self.ask_question("Berapa hasil dari 10 + 5?", "15")
                self.ask_question("Berapa hasil dari 26 - 15?", "11")
                self.ask_question("Berapa hasil dari 8 x 5?", "40")
                self.ask_question("Berapa hasil dari 7 x 3?", "21")
                repeat = input("Apakah Anda ingin mengulangi kuis? (ya/tidak): ").strip().lower()
                if repeat != 'ya':
                    break
        else:
            print("Maaf, Anda belum cukup umur untuk ikut kuis.")
        print(f"Total poin Anda: {self.points}")       

    def ask_question(self, question, answer):
        user_answer = input(question + " ").strip().capitalize()
        if user_answer == answer:
            print("Jawaban Anda benar!")
            self.points += 1
        else:
            print("Jawaban Anda salah.")

def main():
    quiz = Quiz()  # Membuat objek dari kelas Quiz
    
    while True:
        # Meminta input nama dan usia dari pengguna
        name = input("Masukkan nama Anda: ")
        age_input = input("Masukkan usia Anda: ")

        try:
            age = int(age_input)  # Mengonversi input usia ke integer
            quiz.participate_quiz(name, age)  # Memanggil metode untuk memeriksa apakah bisa ikut kuis
            repeat_outer = input("Apakah Anda ingin mengulangi kuis dari awal? (ya/tidak): ").strip().lower()
            if repeat_outer != 'ya':
                break
        except ValueError:
            print("Error! Masukkan usia dalam bentuk angka.")

if __name__ == "__main__":
    main()

















