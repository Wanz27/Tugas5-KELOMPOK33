class Quiz:
    def __init__(self):
        self.points = 0
    
    def participate_quiz(self, name, age):
        if not isinstance(age, int):
            print("Error! Masukkan usia dalam bentuk angka.")
            return
        
        
