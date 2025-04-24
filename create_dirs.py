import os
# this is only for easier to put my questions.
def create_dir_add_description(start, end):
    """
    Belirtilen aralıktaki sayılarla 'problem_X' adında klasörler oluşturur
    ve her klasörün içine 'doldur.md' adında bir dosya ekler.

    Args:
        baslangic (int): Klasör adlandırması için başlangıç sayısı.
        bitis (int): Klasör adlandırması için bitiş sayısı (dahil).
    """
    for i in range(start, end + 1):
        klasor_adi = f"problem_{i}"
        os.makedirs(klasor_adi, exist_ok=True)  # Klasör zaten varsa hata vermez

        dosya_yolu = os.path.join(klasor_adi, f"problem{i}.md")
        with open(dosya_yolu, "w") as dosya:
            dosya.write("doldur")


start = 13
end = 17
create_dir_add_description(start, end)

print(f"{start} ile {end} created between dir's and created .md's.")