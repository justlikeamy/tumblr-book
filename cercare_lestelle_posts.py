import requests

type_list = ['text', 'photo', 'quote', 'link', 'answer', 'video', 'audio', 'chat']
posts_dict = {}

for type in type_list:

    posts_dict[f'{type}_posts'] = []

    api_key = "BDDt1XJlarOmVOiDDK45ao6v4rVgqAdetNaSXbbqdAPeoahqBF"

    # pull first 20 posts
    post_url = f'https://api.tumblr.com/v2/blog/cercare-lestelle.tumblr.com/posts?&api_key={api_key}&type={type}'

    get_posts = requests.get(post_url)
    print(f'GET response: {get_posts}')

    posts_dict[f'{type}_posts'].append(get_posts.json()['response']['posts'])

    # begin pagination
    next_page_key = get_posts.json()['response']['_links']['next']['href']
    
    while next_page_key != None:
        next_page = f'https://api.tumblr.com/{next_page_key}&api_key={api_key}&type={type}'

        get_posts = requests.get(next_page)
        print(f'GET response: {get_posts}')

        posts_dict[f'{type}_posts'].append(get_posts.json()['response']['posts'])

        try:
            next_page_key = get_posts.json()['response']['_links']['next']['href']
        except KeyError:
            next_page_key = None