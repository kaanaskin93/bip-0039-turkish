q = input("Yazı girmek yerine bu klasöre eklediğiniz bir pdf/txt dosyasını giriş olarak kullanmak ister misiniz?")

if q.lower() == "evet":
    def copy_file(input_file, output_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as input_file:
                content = input_file.read()

            with open(output_file, 'w', encoding='utf-8') as output_file:
                output_file.write(content)

            print(f"İçerik kopyalandı.")

        except FileNotFoundError:
            print("Dosya bulunamadı.")
        except Exception as e:
            print(f"HATA. {e}")

    if __name__ == "__main__":
        try:
            input_file = input("Dosyanın uzantısıyla birlikte adını giriniz...")
            output_file = "finals.txt"
            copy_file(input_file, output_file)
        except KeyboardInterrupt:
            print("\nIPTAL.")

        with open('finals.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split() 

        with open('finals.txt', 'w', encoding='utf-8') as file:  
            for word in words:
                file.write(word + '\n')

elif q.lower() == "hayır":
    article = input("Türkçe dilinde herhangi bir yazı girin...")
    lower_article = article.lower()
    with open("finals.txt", "w", encoding="utf-8") as file:
        for line in lower_article.split('\n'):
            words = line.split()
            for word in words:
                file.write(word + "\n")

    print("Okay!")
