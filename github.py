import requests

class GitHubUser:
  def __init__(self, username):
    self.username = username
    self.baseUrl = f"https://api.github.com/users"
  
  def getUserInfo(self):
    url = f"{self.baseUrl}/{self.username}"
    response = requests.get(url)

    if response.status_code == 200:
      user = response.json()
      self.printUserInfo(user)
    else:
      print(f"Hata: {self.username} için kullanıcı bilgileri getirilemiyor")

  def getRepos(self):
    url = f"{self.baseUrl}/{self.username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
      repos = response.json()
      self.printRepos(repos)
    else:
      print(f"Hata: {self.username} kullanıcısı için repolar getirilemiyor")

  @staticmethod
  def printUserInfo(user):
    print(f"\nKullanıcı Adı: {user['login']}")
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

  @staticmethod
  def printRepos(repos):
    for repo in repos:
      print(f"\nRepo Adı: {repo['name']}")
      print(f"Açıklama: {repo['description']}")
      print(f"HTML URL: {repo['html_url']}")
      print(f"Yıldız Sayısı: {repo['stargazers_count']}")
      print(f"Çatallanma Sayısı: {repo['forks_count']}")
      print(f"Açık Konu (issue) Sayısı: {repo['open_issues_count']}")
      print(f"Programlama Dili: {repo['language']}")
      print(f"Lisans: {repo['license']['name'] if repo['license'] else 'Lisans yok'}")
      print(f"Oluşturulma Tarihi: {repo['created_at']}")
      print(f"Güncellenme Tarihi: {repo['updated_at']}")
      print("-" * 41)

def main():
  while True:
    print("GitHub Kullanıcı Bilgileri Aracı")
    print("1. Kullanıcı Bilgilerini Al")
    print("2. Kullanıcı Depolarını Listele")
    print("3. Çıkış")

    choice = input("Seçiminizi girin (1/2/3): ")

    if choice in ['1', '2']:
      githubUsername = input("GitHub kullanıcı adını girin: ")
      user = GitHubUser(githubUsername)
    
      if choice == '1':
        user.getUserInfo()
      elif choice == '2':
        user.getRepos()
    elif choice == '3':
      print("Çıkış yapılıyor...")
      break
    else:
      print("Geçersiz seçim. Lütfen 1, 2 ya da 3 girin.")

if __name__ == "__main__":
    main()