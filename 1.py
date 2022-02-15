import requests


def get_media_url(self, host, media_id):
  web_url = get_url(host, media_id)
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.1462.91 Safari/537.36',
                   'Referer': 'https://{0}/'.format(host)}
  r = requests.(web_url, headers=headers)
  headers.update({'Referer': web_url})
  html = r.content
  match = re.search(r'''dsplayer\.hotkeys[^']+'([^']+).+?function\s*makePlay.+?return[^?]+([^"]+)''', html, re.DOTALL)
  if match:
    token = match.group(2)
    url = 'https://{0}{1}'.format(host, match.group(1))
    html = http_GET(url, headers=headers).content
    return dood_decode(html) + token + str(int(time.time() * 1000)) + helpers.append_headers(headers)

  raise ResolverError('Video Link Not Found')


def dood_decode(self, data):
  t = string.ascii_letters + string.digits
  return data + ''.join([random.choice(t) for _ in range(10)])
