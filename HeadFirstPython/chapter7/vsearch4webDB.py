from flask import Flask, render_template, request, escape
from vsearch import search_for_vowels_by_default_value

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': '***VSearch_123***',
                'database': 'vsearchlogDB',
                }
    # 安装mysql-connector-python 而不是mysql-connector
    import mysql.connector
    conn = mysql.connector.connect(**dbconfig)
    curson = conn.cursor()
    _SQL = """ insert into log (phrase,letters,ip,browser_string,results)
            values
            (%s, %s, %s, %s, %s)"""

    curson.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
    conn.commit()
    curson.close()
    conn.close()
    # with open('vsearch.log', 'a') as log:
    #     print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search_for_vowels_by_default_value(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,
                           )


if __name__ == '__main__':
    app.run(debug=True)
