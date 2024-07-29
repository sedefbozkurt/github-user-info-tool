# github-user-info-tool

## Genel Bakış

GitHub REST API'sini kullanarak GitHub kullanıcısı ve repoları hakkındaki bilgileri alan ve görüntüleyen bir Python uygulamasıdır. Araç şunları yapmanızı sağlar:

- Kullanıcı bilgilerini alma ve görüntüleme
- Bir kullanıcının repolarını listeleme
- Repoları güncellenme tarihlerine göre filtreleme
- Getirilen veriler JSON dosyasına kaydedilir.

## Özelliler

- **Kullanıcı Bilgilerinin Alınması**: GitHub kullanıcısı hakkındaki bilgileri alır ve görüntüler
- **Repo Listesi**: Bir kullanıcının tüm repolarını listeler
- **Tarihe Göre Filtreleme**: Belirli bir tarih aralığında güncellenen veri havuzlarını filtreler
- **Veri Kaydetme**: Getirilen kullanıcı ve repo bilgilerini JSON dosyalarına kaydeder.

## Kurulum

1. **Repoyu Klonlayın**:

    ```sh
    git clone https://github.com/sedefbozkurt/github-user-info-tool.git
    cd github-user-info-tool
    ```

2. **Gerekli Paketleri Yükleyin**:

    ```sh
    pip install requests
    ```

3. **API Anahtarını Ayarlayın**:

    GitHub API'sini kullanmak için bir kişisel erişim anahtarına ihtiyacınız olacak. Bu anahtarı bir `.env` dosyasına ekleyin:

    ```env
    GITHUB_API_KEY=your_api_key_here
    ```

## Kullanım

Uygulamayı çalıştırmak için:

```sh
python github_user_info.py
