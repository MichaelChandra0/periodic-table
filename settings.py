
class Settings:

    def __init__(self):
        self.active = False
        self.elements_location = "data/elements.json"

        self.elements = None

        self.menu="""
TABEL PERIODIK
1. Lihat nama element
2. Informasi lebih detail mengenai element
3. Menambahkan element baru
4. Memperbarui element
5. Menghapus element
q. Exit
"""