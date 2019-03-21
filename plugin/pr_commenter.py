import requests
import vim

class VimExt:
    def __init__(self):
        vim.command('vnew')

    def print_lines(self, comments):
        [self.prints(i) for i in comments]

    def prints(self, line):
        vim.current.line = line

        w = vim.current.window
        w.height += 1
        print(w.cursor, vim.current.buffer[0])

class PrCommenter:
    PR_API_ENDPOINT='https://api.github.com/repos/{}/{}/'

    def __init__(self, prof, repo):
        self.url = self.PR_API_ENDPOINT.format(prof, repo)

    def comments_get(self):
        comments_endpoint = self.url + 'pulls/191/comments'
        resp = requests.get(url=comments_endpoint)
        data = resp.json()

        self.comments = []
        for i in data:
            self.comments.append({
                    'user': i['user']['login'],
                    'body': i['body'],
                    'diff': i['diff_hunk'],
                    })

    def comments_output(self):
        ret = []
        cmd_template = '#USER: {} - Comment: {}'
        for i in self.comments:
            ret.append(cmd_template.format(i['user'], i['body']))

        return ret
        

if __name__ == '__main__':
    pr = PrCommenter('bisdn', 'basebox')
    pr.comments_get()
