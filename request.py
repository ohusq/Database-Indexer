import bs4 as bs
import requests

def get_data(username: str, password: str) -> list:
    """
    Grabs the data from the server, returns in a list [[username, password], [username, password], [username, password
    """
    url = f"http://localhost:5000/search?search={username}&select=username"
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, 'html.parser')
    usernames = [username.text for username in soup.find_all('td', class_='r_username')]
    passwords = [password.text for password in soup.find_all('td', class_='r_password')]
    _list = [[usernames[i], passwords[i]] for i in range(len(usernames))]
    return _list

username = "admin"
password = "password"

data = get_data(username, password)

print(data[0]) # ['admin', 'password']