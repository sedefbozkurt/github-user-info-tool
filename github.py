import json
import requests
from datetime import datetime

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
      self.writeToFile("userInfo.json", user)
    else:
      print(f"Hata: {self.username} için kullanıcı bilgileri getirilemiyor")

  def getRepos(self, startDate=None, endDate=None):
    url = f"{self.baseUrl}/{self.username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
      repos = response.json()
      filteredRepos = self.filterReposByDate(repos, startDate, endDate) if startDate and endDate else repos
      self.printRepos(filteredRepos)
      self.writeToFile("repos.json", filteredRepos)
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

  @staticmethod
  def writeToFile(fileName, data):
    with open(fileName, 'w') as f:
      json.dump(data, f, indent=3)
    print(f"Veriler {fileName} dosyasına yazıldı")

  @staticmethod
  def filterReposByDate(repos, startDate, endDate):
    startDate = datetime.strptime(startDate, "%Y-%m-%d")
    endDate = datetime.strptime(endDate, "%Y-%m-%d")
    filteredRepos = [
      repo for repo in repos
      if startDate <= datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ") <= endDate
    ]
    return filteredRepos

def main():
  while True:
    print("\nGitHub Kullanıcı Bilgileri Aracı")
    print("1. Kullanıcı Bilgilerini Al")
    print("2. Kullanıcı Depolarını Listele")
    print("3. Belirli Bir Tarih Aralığındaki Kullanıcı Repolarını Listele")
    print("4. Çıkış")

    choice = input("Seçiminizi girin (1/2/3/4): ")

    if choice in ['1', '2', '3']:
      githubUsername = input("GitHub kullanıcı adını girin: ")
      user = GitHubUser(githubUsername)
    
      if choice == '1':
        user.getUserInfo()
      elif choice == '2':
        user.getRepos()
      elif choice == '3':
        startDate = input("Başlangıç ​​tarihini girin (YYYY-AA-GG): ")
        endDate = input("Bitiş ​​tarihini girin (YYYY-AA-GG): ")
        user.getRepos(startDate, endDate)
    elif choice == '4':
      print("Çıkış yapılıyor...")
      break
    else:
      print("Geçersiz seçim. Lütfen 1, 2, 3 ya da 4 girin.")

if __name__ == "__main__":
    main()