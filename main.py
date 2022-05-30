from datetime import datetime
import time
import sys
from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__, template_folder='templates')

start_times = []
end_times = []


def calculate(start_date, end_date):
    output = []
    # get_dates(start_date, end_date)
    # start_str = start_date[:-3]+start_date[-2:]
    start_date_unix = datetime.strptime(start_date, "%Y-%m-%d").timestamp()
    # start_times.append(datetime.strptime(start_date, "%Y-%m-%d"))
    start_times.append(start_date_unix)
    print(start_date_unix)
    print(f"start list: {start_times}")
    end_date_unix = datetime.strptime(end_date, "%Y-%m-%d").timestamp()
    print(end_date_unix)
    # end_times.append(datetime.strptime(end_date, "%Y-%m-%d"))
    end_times.append(end_date_unix)
    print(f"end list: {end_times}")

    all_times = start_times + end_times
    # print(all_times)
    all_times.sort()
    # print(all_times)

    counter = 0
    max_counter = 0
    max_counter_date = None

    for date in all_times:
        if date in start_times and date in end_times:
            # print(1)
            continue
        elif date in start_times:
            # print(2)
            counter += 1
        else:
            # print(3)
            counter -= 1

        if counter > max_counter:
            max_counter = counter
            max_counter_date = date

    print(f"counter: {max_counter}")
    print(f"date: {max_counter_date}")
    if max_counter <= 1:
        # print("No times could be found that suited everyone!")
        output.append("N/A")
        output.append("N/A")

    else:
        output.append(datetime.utcfromtimestamp(int(max_counter_date + 4000)).strftime('%Y-%m-%d'))
        output.append(max_counter)
        # print(f"The date that suits {max_counter} people is "
        #       f"{datetime.utcfromtimestamp(int(max_counter_date)).strftime('%Y-%m-%d')}")

    return output


@app.route('/')
def index():
    return render_template('index.html', date="N/A", amount="N/A")


@app.route('/', methods=['POST'])
def html_input():
    start_date = request.form['start']
    end_date = request.form['end']
    # print(start_date)
    # print(end_date)
    calc_output = calculate(start_date, end_date)
    optimal_date = calc_output[0]
    best_for = calc_output[1]
    # optimal_date = calculate()[0]
    # best_for = calculate()[1]

    return render_template('index.html', date=optimal_date, amount=best_for)


if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True)

    # Production
    http_server = WSGIServer(('', 6565), app)
    http_server.serve_forever()
