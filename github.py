import requests

def getGithubUserInfo(username):
  url = f"https://api.github.com/users/{username}"
  response = requests.get(url)

  if response.status_code == 200:
    user = response.json()
    print(f"Kullanıcı Adı: {user['login']}")
    print(f"Tam Adı: {user['name']}")
    print(f"Profil URL: {user['html_url']}")
    print(f"Takipçi Sayısı: {user['followers']}")
    print(f"Takip Edilen Kişi Sayısı: {user['following']}")
    print(f"Hesabın Oluşturulma Tarihi: {user['created_at']}")
    print(f"Bio: {user['bio']}")
    print(f"Konum: {user['location']}")
    print(f"Blog: {user['blog']}")
    print(f"Email: {user['email']}")
    print("-" * 41)
  else:
    print(f"Hata: {username} için kullanıcı bilgileri getirilemiyor")

def getGithubRepos(username):
  url = f"https://api.github.com/users/{username}/repos"
  response = requests.get(url)

  if response.status_code == 200:
    repos = response.json()
    for repo in repos:
      print(f"Repo Adı: {repo['name']}")
      print(f"Açıklama: {repo['description']}")
      print(f"HTML URL: {repo['html_url']}")
      print(f"Yıldız Sayısı: {repo['stargazers_count']}")
      print(f"Çatallanma Sayısı: {repo['forks_count']}")
      print(f"Açık Konu (issue) Sayısı: {repo['open_issues_count']}")
      print(f"Programlama Dili: {repo['language']}")
      print(f"Lisans: {repo['licence']['name'] if repo['licence'] else 'Lisans yok'}")
      print(f"Oluşturulma Tarihi: {repo['created_at']}")
      print(f"Güncellenme Tarihi: {repo['updated_at']}")
      print("-" * 41)
  else:
    print(f"Hata: {username} kullanıcısı için repolar getirilemiyor")

def main():
  while True:
    print("GitHub Kullanıcı Bilgileri Aracı")
    print("1. Kullanıcı Bilgilerini Al")
    print("2. Kullanıcı Depolarını Listele")
    print("3. Çıkış")

    choice = input("Seçiminizi girin (1/2/3): ")

    if choice == '1':
      githubUsername = input("GitHub kullanıcı adını girin: ")
      getGithubUserInfo(githubUsername)
    elif choice == '2':
      githubUsername = input("GitHub kullanıcı adını girin: ")
      getGithubRepos(githubUsername)
    elif choice == '3':
      print("Çıkış yapılıyor...")
      break
    else:
      print("Geçersiz seçim. Lütfen 1, 2 ya da 3 girin.")

if __name__ == "__main__":
    main()