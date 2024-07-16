import csv


def view1():
    return ['<h1>Welcome to the Front Page</h1>']


def view2(create=False, user=None):
    html = ['Create new user: <form action="" method="post">\n',
            '<input type="text" placeholder="username">\n', 
            '<input type="text" placeholder="email">\n', 
            '<input type="submit"></form>\n']  
    if create:
        with open('app_users.csv', 'a') as fhandle:
            writer = csv.writer(fhandle)
            writer.writerow(user)
    with open('app_users.csv', 'r') as fhandle:
        html.append('Users: <ul>\n')
        reader = csv.DictReader(fhandle)
        for row in reader:
            html.append(f'<li> {row["username"]} | {row["email"]} </li>\n')
        html.append('</ul>')
    return html

    

